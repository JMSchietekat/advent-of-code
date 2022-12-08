import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '/day_08_input_sample.txt'
INPUT_PATH = ROOT_DIR + "/day_08_input.txt"

def p1(path):
    
    M = []

    with open(path) as f:
        for l in f:
            R = []
            for i in l.strip():
                R.append([int(i),0])
            M.append(R)

    W = len(M)
    H = len(M[0])
    
    for c in range(1,H-1):
        for r in range(1,W-1):
            for ri in range(r+1,W):
                if M[r][c][0] <= M[ri][c][0]:
                    break 
                elif ri == W-1:
                    M[r][c][1] += 1
            
            for ci in range(c+1,H):
                if M[r][c][0] <= M[r][ci][0]:
                    break 
                elif ci == H-1:
                    M[r][c][1] += 1

            for ri in range(r-1,-1,-1):
                if M[r][c][0] <= M[ri][c][0]:
                    break 
                elif ri == 0:
                    M[r][c][1] += 1
            
            for ci in range(c-1,-1,-1):
                if M[r][c][0] <= M[r][ci][0]:
                    break 
                elif ci == 0:
                    M[r][c][1] += 1 
                    

    score = 2 * (H-1) + 2 * (W-1)

    for r in range(1,H-1):
        for c in range(1,W-1):
            if M[r][c][1] > 0:
                score += 1
    
    return score

def p2(path):
    M = []

    with open(path) as f:
        for l in f:
            R = []
            for i in l.strip():
                R.append([int(i),0])
            M.append(R)

    W = len(M)
    H = len(M[0])
    
    for c in range(1,H-1):
        for r in range(1,W-1):
            s = [0,0,0,0]
            for ri in range(r+1,W):
                s[0] += 1
                if M[r][c][0] <= M[ri][c][0]:
                    break                
            
            for ci in range(c+1,H):
                s[1] += 1
                if M[r][c][0] <= M[r][ci][0]:
                    break

            for ri in range(r-1,-1,-1):
                s[2] += 1 
                if M[r][c][0] <= M[ri][c][0]:
                    break
            
            for ci in range(c-1,-1,-1):
                s[3] += 1 
                if M[r][c][0] <= M[r][ci][0]:
                    break
            
            M[r][c][1] = s[0] * s[1] * s[2] * s[3]
                    
    score = 0    

    for r in range(1,H-1):
        for c in range(1,W-1):
            if M[r][c][1] > score:
                score = M[r][c][1]
    
    return score


if __name__ == "__main__":

    print(p1(SAMPLE_INPUT_PATH))
    print(p1(INPUT_PATH))

    print(p2(SAMPLE_INPUT_PATH))
    print(p2(INPUT_PATH))