import os 
from dotenv import load_dotenv

load_dotenv()
my_id = os.getenv("Command_symbol")
def handle_response(message) -> str:
    message_lower = message.lower()
    #ignore non commands
    if message_lower[0] != my_id:
        return
    message_lower = message_lower[1:]
    #procces text
    if message_lower == "start":
        return "The Server is starting!"
    elif message_lower == "status":
        return "The Server does not Exist"
    else:
        return "Unrecognized command"
