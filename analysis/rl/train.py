from collections import deque, namedtuple
import random
import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential, load_model
import pandas as pd


class Agent:
    def __init__(
        self,
        number_of_shares,
        epsilon=1,
        epsilon_decay=0.998,
        epsilon_end=0.01,
        gamma=0.99,
    ):
        self.number_of_shares = number_of_shares
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_end = epsilon_end
        self.gamma = gamma
        self.model = self.build_model()

    def build_model(self):
        # Create a sequential model with 3 layers
        model = Sequential(
            [
                # Input layer expects a flattened grid, hence the input shape is grid_size squared
                Dense(128, activation="relu", input_shape=(self.number_of_shares,)),
                Dense(64, activation="relu"),
                # Output layer with number of shares units for the possible actions (up, down, left, right)
                Dense(self.number_of_shares, activation="linear"),
            ]
        )

        model.compile(optimizer="adam", loss="mse")

        return model

    def get_action(self, state):
        # rand() returns a random value between 0 and 1
        if np.random.rand() <= self.epsilon:
            # Exploration: random action
            action = np.random.randint(0, 4)
        else:
            # Add an extra dimension to the state to create a batch with one instance
            state = np.expand_dims(state, axis=0)

            # Use the model to predict the Q-values (action values) for the given state
            q_values = self.model.predict(state, verbose=0)

            # Select and return the action with the highest Q-value
            action = np.argmax(
                q_values[0]
            )  # Take the action from the first (and only) entry

        # Decay the epsilon value to reduce the exploration over time
        if self.epsilon > self.epsilon_end:
            self.epsilon *= self.epsilon_decay

        return action

    def learn(self, experiences):
        states = np.array([experience.state for experience in experiences])
        actions = np.array([experience.action for experience in experiences])
        rewards = np.array([experience.reward for experience in experiences])
        next_states = np.array([experience.next_state for experience in experiences])
        dones = np.array([experience.done for experience in experiences])

        # Predict the Q-values (action values) for the given state batch
        current_q_values = self.model.predict(states, verbose=0)

        # Predict the Q-values for the next_state batch
        next_q_values = self.model.predict(next_states, verbose=0)

        # Initialize the target Q-values as the current Q-values
        target_q_values = current_q_values.copy()

        # Loop through each experience in the batch
        for i in range(len(experiences)):
            if dones[i]:
                # If the episode is done, there is no next Q-value
                # [i, actions[i]] is the numpy equivalent of [i][actions[i]]
                target_q_values[i, actions[i]] = rewards[i]
            else:
                # The updated Q-value is the reward plus the discounted max Q-value for the next state
                # [i, actions[i]] is the numpy equivalent of [i][actions[i]]
                target_q_values[i, actions[i]] = rewards[i] + self.gamma * np.max(
                    next_q_values[i]
                )

        # Train the model
        self.model.fit(states, target_q_values, epochs=1, verbose=0)

    def load(self, file_path):
        self.model = load_model(file_path)

    def save(self, file_path):
        self.model.save(file_path)


class Environment:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.row = []
        self.agent_location = None
        self.goal_location = None

    def reset(self):
        # Initialize the empty grid as a 2d array of 0s
        self.row = np.zeros((self.grid_size, self.grid_size))

        # Return the initial state of the grid
        return self.get_state()


    def get_state(self):
        # Flatten the grid from 2d to 1d
        state = self.row.flatten()
        return state

    def is_valid_location(self, location):
        # Check if the location is within the boundaries of the grid
        if (0 <= location[0] < self.grid_size) and (0 <= location[1] < self.grid_size):
            return True
        else:
            return False

    def step(self, action):
        # Apply the action to the environment, record the observations
        reward, done = self.move_agent(action)
        next_state = self.get_state()

        return reward, next_state, done


class ExperienceReplay:
    def __init__(self, capacity, batch_size):
        # Memory stores the experiences in a deque, so if capacity is exceeded it removes
        # the oldest item efficiently
        self.memory = deque(maxlen=capacity)

        # Batch size specifices the amount of experiences that will be sampled at once
        self.batch_size = batch_size

        # Experience is a namedtuple that stores the relevant information for training
        self.Experience = namedtuple(
            "Experience", ["state", "action", "reward", "next_state", "done"]
        )

    def add_experience(self, state, action, reward, next_state, done):
        # Create a new experience and store it in memory
        experience = self.Experience(state, action, reward, next_state, done)
        self.memory.append(experience)

    def sample_batch(self):
        # Batch will be a random sample of experiences from memory of size batch_size
        batch = random.sample(self.memory, self.batch_size)
        return batch

    def can_provide_sample(self):
        # Determines if the length of memory has exceeded batch_size
        return len(self.memory) >= self.batch_size


def train(df: pd.DataFrame):
    grid_size = len(df.columns)

    environment = Environment(grid_size=grid_size)
    agent = Agent(
        number_of_shares=grid_size, epsilon=1, epsilon_decay=0.9998, epsilon_end=0.01
    )
    experience_replay = ExperienceReplay(capacity=10000, batch_size=32)
    # agent.load(f'models/model_{grid_size}.h5')

    # Number of episodes to run before training stops
    episodes = 5000
    # Max number of steps in each episode
    max_steps = 250

    for episode in range(episodes):
        # Get the initial state of the environment and set done to False
        state = environment.reset()

        # Loop until the episode finishes
        for step in range(max_steps):
            print("Episode:", episode)
            print("Step:", step)
            print("Epsilon:", agent.epsilon)

            # Get the action choice from the agents policy
            action = agent.get_action(state)

            # Take a step in the environment and save the experience
            reward, next_state, done = environment.step(action)
            experience_replay.add_experience(state, action, reward, next_state, done)

            # If the experience replay has enough memory to provide a sample, train the agent
            if experience_replay.can_provide_sample():
                experiences = experience_replay.sample_batch()
                agent.learn(experiences)

            # Set the state to the next_state
            state = next_state

            if done:
                break

            # Optionally, pause for half a second to evaluate the model
            # time.sleep(0.5)

        agent.save(f"models/model_{grid_size}.h5")
