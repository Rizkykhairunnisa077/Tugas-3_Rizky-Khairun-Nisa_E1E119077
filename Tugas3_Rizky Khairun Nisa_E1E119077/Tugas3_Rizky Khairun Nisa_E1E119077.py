class GameEntry:
    total_player = 0

    def __init__(self, nama, score, times):
        self.nama = nama
        self.score = score
        self.times = times
        
        GameEntry.total_player += 1
    
    def setName(self, nama):
        self.nama = nama

    def getName(self):
        return self.nama

    def setScore(self, score):
        self.score = score
    
    def getScore(self):
        return self.score

    def setTime(self, times):
        self.times = times

    def getTime(self):
        return self.times

    def getTotal():
        return GameEntry.total_player

class ScoreBoard:

    def __init__(self, capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        self.n = 0 
    
    def getCapacity(self):
        return self.capacity

    def sumEntries(self):
        return self.n

    def addItem(self, entry):
        score = entry.getScore()

        condition = len(self.board) > self.n or score > self.board[self.capacity - 1].getScore()

        if condition:
            if self.n < self.capacity:
                self.n += 1

            j = self.n - 1

            while j > 0 and self.board[j-1].getScore() < score:
                self.board[j] = self.board[j-1]
                j -= 1
            self.board[j] = entry
            print(f"Entri {score} Berhasil ditambahkan!")

    def listEntries(self):
        for i in range (0, self.n):
            print(i+1,":", getattr(self.board[i], 'nama'), getattr(self.board[i], 'score'))

board = ScoreBoard(10)

active = True

while active:
    print("")
    start = input("Pilih Salah Satu \n 1 = Menambahkan Entry Baru \n 2 = Mampilkan List ScoreBoard \n 3 = Keluar \n")
    print("")
    print("Masukkan Data Entry: ")
    
    if start == '2':
        board.listEntries()
    elif start == '1':
        nama = input("Masukkan Nama Pemain ")
        skor = int(input("Masukkan Score "))
        waktu = int(input("Masukkan Waktu "))

        in_score = GameEntry(nama, skor, waktu)
        set_board = board.addItem(in_score)

        print(f"Entri baru ditambahkan:{in_score.getName()} {in_score.getScore()} {in_score.getTime()}")
    else:
        break
