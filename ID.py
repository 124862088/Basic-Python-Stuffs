import time


class Person(object):

    def __init__(self,first_name,last_name,gender,age):
        self.first_name = str(first_name).title()
        self.last_name = str(last_name).title()
        self.gender = str(gender).title()
        self.age = int(age)

    def greeting(self):
        # Below 3 conditions in one line.
        print(f"[+] Hello dear "
              f"{'Mrs.' if self.gender == 'Female' else 'Mr.' if self.gender == 'Male' else ''}"
              f"{self.last_name}")
        print("[+] Welcome to the club!" if self.age >= 18 else "[-] You are not over 18 yet.")

    def __str__(self):
        # For a print() of every single instance
        return f"\t\tYour ID:" \
               f"\n\tName: {self.first_name +' '+self.last_name} " \
               f"\n\tGender: {self.gender}" \
               f"\n\tAge:{self.age}" \
               # f"\n\t{time.strftime('%d/%b/%Y %H:%M')}"

    # def create_file(self):
    #     filename = input("Enter the file name: ")
    #     with open(f'{filename}.txt','x') as file:
    #         try:
    #             print(f'[+] File {filename} successfully created!')
    #         except:
    #             print(f'Something wrong happened - Please check')
    #         finally:
    #             file.close()

    def write_file(self):
        #Record the personal ID in the file.
        with open('test.txt','w') as test:
            try:
                test.write(self.__str__() + '\n\t\tLast Update: '
                           + time.strftime('%d/%b/%Y %H:%M'))
                print("[+] Writedown successful")
            except:
                print("[-] Error happened - Please check your setting")
            finally:
                test.close()

    def read_file(self):
        # Read the personal ID from the file.
        with open('test.txt','r') as test:
            try:
                print("[+] Read successful: ")
                print(test.read())
            except:
                print("[-] Error happened - Please check your setting")
            finally:
                test.close()


if __name__ == '__main__':
    person2 = Person("first","last","male",19)
    person2.greeting()
    person2.write_file()
    person2.read_file()
    # print(person2)