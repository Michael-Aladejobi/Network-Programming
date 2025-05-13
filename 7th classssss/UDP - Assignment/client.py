import socket
import pickle


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 7001)

print("Client started...")

msg = input('Say hello to server: ')
msg = str.encode(msg)
client_socket.sendto(msg, server_address)


game_array_data, _ = client_socket.recvfrom(1024)
game_array = pickle.loads(game_array_data)
print("Game array:", game_array)

selected_index = input("Enter an index from 0 - 3: ")
while selected_index.strip().lower() != "bye":
    client_socket.sendto(selected_index.encode(), server_address)

    selected_value = input("Enter a value from 1 - 9: ")
    client_socket.sendto(selected_value.encode(), server_address)

    updated_game_array, _ = client_socket.recvfrom(1024)
    if updated_game_array == b"win":
        print("Congratulations! You won!")
        break

    game_array = pickle.loads(updated_game_array)
    print("Game array after your move:", game_array)

    updated_game_array, _ = client_socket.recvfrom(1024)
    if updated_game_array == b"win":
        print("Client wins! Game over.")
        break

    game_array = pickle.loads(updated_game_array)
    print("Game array after server's move:", game_array)

    if all(element == 0 for element in game_array):
        print("Server wins! Game over.")
        break

    selected_index = input("Enter an index from 0 - 3 or type 'bye' to quit: ")

client_socket.sendto(b"bye", server_address)
client_socket.close()