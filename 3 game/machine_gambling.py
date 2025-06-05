import random
import os 


SO_TIEN_BAN_DAU = 10.00 
TIEN_MOI_LUOT = 0.25      
AN_2_NHAY = 0.50  
AN_3_NHAY = 10.00 
SAVE_GAME = "Save_game.txt" 


class Machine_Glambing:
    
    def __init__(self):
        
        pass

    def _generate_spin(self):
        
        digit1 = random.randint(0, 9)
        digit2 = random.randint(0, 9)
        digit3 = random.randint(0, 9)
        return (digit1, digit2, digit3)

    def _calculate_winnings(self, digits):
        
        d1, d2, d3 = digits

        
        if d1 == d2 == d3:
            return AN_3_NHAY
        
        
        elif d1 == d2 or d1 == d3 or d2 == d3:
            return AN_2_NHAY
        
       
        else:
            return 0.00

    def play_round(self, current_balance):
        
        
        print("\n--- Quay số... ---")
        digits = self._generate_spin()
        print(f"Kết quả: {digits[0]} {digits[1]} {digits[2]}")

        winnings = self._calculate_winnings(digits)
        
        if winnings > 0:
            print(f"Chúc mừng! Bạn đã thắng ${winnings:.2f}!")
        else:
            print("Chúc may mắn lần sau!")
            
        return winnings, digits


class Manager:
    
    def __init__(self):
        
        self.slot_machine = Machine_Glambing()
        self.balance = self._load_balance() 
        print(f"Chào mừng bạn đến với Máy đánh bạc! Số tiền hiện tại của bạn: ${self.balance:.2f}")

    def _load_balance(self):
        
        if os.path.exists(SAVE_GAME):
            try:
                with open(SAVE_GAME, 'r') as f:
                    balance_str = f.read().strip()
                    if balance_str: 
                        return float(balance_str)
                    else:
                        print(f"File '{SAVE_GAME}' trống. Khởi tạo lại số tiền ban đầu.")
                        return SO_TIEN_BAN_DAU
            except ValueError:
                print(f"Lỗi đọc số tiền từ file '{SAVE_GAME}'. Khởi tạo lại số tiền ban đầu.")
                return SO_TIEN_BAN_DAU
            except Exception as e:
                print(f"Lỗi không xác định khi tải file: {e}. Khởi tạo lại số tiền ban đầu.")
                return SO_TIEN_BAN_DAU
        else:
            print(f"Không tìm thấy file '{SAVE_GAME}'. Bắt đầu với số tiền ban đầu.")
            return SO_TIEN_BAN_DAU

    def _save_balance(self):
        
        try:
            with open(SAVE_GAME, 'w') as f:
                f.write(str(self.balance))
            print(f"Trò chơi đã được lưu. Số tiền hiện tại: ${self.balance:.2f}")
        except Exception as e:
            print(f"Lỗi khi lưu trò chơi: {e}")

    def _display_menu(self):
        
        print("\n--- Menu ---")
        print("1. Chơi máy đánh bạc")
        print("2. Lưu trò chơi")
        print("3. Rút tiền (Cash out)")
        print(f"Số tiền của bạn: ${self.balance:.2f}")

    def _get_user_choice(self):
        
        while True:
            try:
                choice = int(input("Chọn hành động của bạn (1, 2, hoặc 3): "))
                
                return choice
            except ValueError:
                print("Vui lòng nhập một số nguyên.")

    def run_game(self):
        
        running = True
        while running:
           
            if self.balance < TIEN_MOI_LUOT:
                print("\n--- HẾT TIỀN! ---")
                print("Bạn không còn đủ tiền để chơi tiếp. Tạm biệt!")
                running = False 
                
                self._save_balance() 
                break

            self._display_menu()
            choice = self._get_user_choice()

            if choice == 1: 
                self.balance -= TIEN_MOI_LUOT
                print(f"Bạn đã mất ${TIEN_MOI_LUOT:.2f}. Số tiền còn lại: ${self.balance:.2f}")
                
                winnings, digits = self.slot_machine.play_round(self.balance)
                self.balance += winnings
                print(f"Số tiền mới của bạn: ${self.balance:.2f}")

            elif choice == 2: 
                self._save_balance()

            elif choice == 3: 
                print(f"\nCảm ơn bạn đã chơi! Số tiền còn lại của bạn: ${self.balance:.2f}")
                self._save_balance() 
                running = False
                break 


if __name__ == "__main__":
    game = Manager()
    game.run_game()