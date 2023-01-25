import numpy as np

def main():
    getWinLossRecord(3, 9)

def getWinLossRecord(gamesPlayed, totalPoints):
    m_list = [[4,1],[1,1]]
    A = np.array(m_list)
    inv_A = np.linalg.inv(A)
    B = np.array([totalPoints,gamesPlayed])
    X = np.linalg.inv(A).dot(B)
    print(X)
if __name__ == "__main__":
    main()