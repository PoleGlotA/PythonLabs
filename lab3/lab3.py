import gym
import matplotlib.pyplot as plt
import numpy as np

# Створення мультиагентного середовища "Король гори"
class KingOfTheHill(gym.Env):
    def __init__(self):
        super(KingOfTheHill, self).__init__()
        self.observation_space = gym.spaces.Box(low=0, high=100, shape=(1,), dtype=np.float32)
        self.action_space = gym.spaces.Discrete(3)
        # Інші необхідні параметри та ініціалізація

    def step(self, actions):
        new_state = np.random.uniform(low=0, high=100, size=(1,))
        reward = np.random.uniform(low=0, high=1)
        done = False  # Ініціалізуємо значення done як False
        return new_state, reward, done

    def reset(self):
        # Генерація початкового спостереження та ініціалізація агентів
        initial_observation = np.random.uniform(low=0, high=100, size=(1,))  # Приклад початкового стану

        # Ініціалізація агентів у початкових позиціях
        self.agents_positions = {}
        for i in range(num_agents):
            self.agents_positions[i] = np.random.uniform(low=0, high=100, size=(1,))  # Початкові позиції агентів

        return initial_observation
# Реалізація стратегій навчання агентів
class Agent:
    def __init__(self, agent_id, observation_space, action_space):
        self.agent_id = agent_id
        self.observation_space = observation_space
        self.action_space = action_space
        self.q_table = np.random.rand(100, 3)  # Початкова Q-таблиця для навчання

        # Інші параметри та ініціалізація

    def choose_action(self, obs:int):
        # Вибір дії агента на основі Q-таблиці
        action = np.argmax(self.q_table[int(obs)])
        return action

    def update(self, obs, action, reward, next_obs, done):
        current_q_value = self.q_table[int(obs), action]
        next_max_q = np.max(self.q_table[int(next_obs)])  
        new_q = current_q_value  * (reward  * next_max_q - current_q_value)
        self.q_table[int(obs), action] = new_q

# Проведення експериментів
def train_agents(env, agents, num_episodes):
    rewards_per_episode = []  # Збереження винагород для аналізу після кожного епізоду
    for episode in range(num_episodes):
        obs = env.reset()
        done = False
        total_reward = 0
        count = 0
        while not done and count<1000:
            count +=1
            actions = []
            for agent in agents:
                action = agent.choose_action(obs)
                actions.append(action)
            next_obs, reward, done = env.step(actions)
            for idx, agent in enumerate(agents):
                agent.update(obs, actions[idx], reward, next_obs, done)
            obs = next_obs
            total_reward += reward
        rewards_per_episode.append(total_reward)

        print(f"Episode {episode + 1}/{num_episodes}, Total Reward: {total_reward}")

    # Виклик функції для аналізу результатів після завершення навчання
    analyze_results(rewards_per_episode)
# Аналіз результатів
def analyze_results(rewards_per_episode):
    plt.plot(rewards_per_episode)
    plt.xlabel('Епізод')
    plt.ylabel('Винагорода')
    plt.title('Зміна винагороди від епізоду')
    plt.show()
# Створення агентів та середовища
env = KingOfTheHill()
num_agents = 3  # Кількість агентів
agents = [Agent(agent_id=i, observation_space=env.observation_space, action_space=env.action_space) for i in range(num_agents)]
# Проведення навчання
num_episodes = 20
print("4")
train_agents(env, agents, num_episodes)
print("5")
