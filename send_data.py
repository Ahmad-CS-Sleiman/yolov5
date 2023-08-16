
import socket
import json


def send_data(label,xyxy):
    
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.0.152", 8888))  # Connect to the server's IP and port

    # while True:
        # message = input("Enter a message: ")
        # if message == "":
        #     print("Message is empty. Not sending.")
        # elif message.lower() == "sleep":
        #     print("Okay, I'm sleeping.")
            # You can implement a sleep here if needed
        # else:
    # print(message)
    
    # Send the message to the server

    # Create a dictionary
    data = {
        "label": label,
        "xyxy": xyxy
    }

    json_data=json.dump(data).encode()

    # client_socket.send(message.encode("utf-8"))

        # Send JSON data
    client_socket.sendall(json_data)

    # Receive and print the response from the server
    response = client_socket.recv(1024).decode("utf-8")
    print("Server response:", response)

    # Close the socket when done
    client_socket.close()



# import json

# # Sample data
# label = "car"
# xyxy = [100, 200, 300, 400]

# # Create a dictionary
# data = {
#     "label": label,
#     "xyxy": xyxy
# }

# # Write the dictionary to a JSON file
# output_filename = "output.json"
# with open(output_filename, "w") as json_file:
#     json.dump(data, json_file)

# print(f"JSON data written to {output_filename}")



