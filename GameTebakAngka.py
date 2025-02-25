
import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("Belum ada skor terbaru, ayo dapatkan skor tertinggi sekarang!")
    else:
        print("Skor tertinggi terakhir adalah {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Selamat datang di permainan tebak angka!")
    player_name = input("Siapa namamu? ")
    wanna_play = input("Halo, {}, Kamu mau main game tebak-tebakan? (Tekan Ya/Tidak) ".format(player_name))
    # // Where the show_score function USED to be
    attempts = 0
    show_score()
    while wanna_play.lower() == "ya":
        try:
            guess = input("Pilih sebuah angka antara 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Silakan tebak angka dengan jangkauan yang diberikan")
            if int(guess) == random_number:
                print("Bagus Sekali!")
                attempts += 1
                attempts_list.append(attempts)
                print("Dia membawamu! {} attempts".format(attempts))
                play_again = input("Kamu mau bermain lagi? (Tekan Ya/Tidak) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "tidak":
                    print("Keren! Ayo coba lagi!")
                    break
            elif int(guess) > random_number:
                print("Lebih rendah")
                attempts += 1
            elif int(guess) < random_number:
                print("Lebih tinggi")
                attempts += 1
        except ValueError as err:
            print("Oh Tidak!, itu bukan angka yang valid. Ayo coba lagi!...")
            print("({})".format(err))
    else:
        print("Keren! Ayo coba lagi!")
if __name__ == '__main__':
    start_game()