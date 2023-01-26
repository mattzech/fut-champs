import numpy as np

def main():
    record = getWinLossRecord(10, 40)
    print(record)
def getWinLossRecord(gamesPlayed, totalPoints):
    m_list = [[4,1],[1,1]]
    A = np.array(m_list)
    inv_A = np.linalg.inv(A)
    B = np.array([totalPoints,gamesPlayed])
    X = np.linalg.inv(A).dot(B)
    wins = int(X[0])
    losses = int(X[1])
    return wins,losses
if __name__ == "__main__":
    main()