import random
import matplotlib.pyplot as plt

MAX_PEOPLE = 50
NUM_RUNS = 1_000


def main():
    '''Calculate the probability of 2 people sharing a birthday.'''
    people_list = []
    prob_list = []
    print('Probability of atleast 2 people sharing a birthday:\n')

    for people in range(2, MAX_PEOPLE + 1):
        shared_birthdays = 0
        # Run multiple sims for group
        for run in range(NUM_RUNS):
            birthdays = []
            # Generate random birthdays for groyp
            for i in range(0, people):
                birthday = random.randrange(0, 364)  # Say no leap years
                birthdays.append(birthday)
            # Share birthday of set has fewer than all birthdays
            if len(set(birthdays)) < len(birthdays):
                shared_birthdays += 1
        prob = (shared_birthdays/NUM_RUNS) * 100
        people_list.append(people)
        prob_list.append(prob)
        print(f'Number people: {people:>2} | Probability = {prob:.2f}%')

    plt.plot(people_list, prob_list, marker='o')
    plt.title('Probability of Shared Birthday')
    plt.xlabel('Number of People')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
