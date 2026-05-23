#!/bin/bash

RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
BLUE='\033[0;94m'
PURPLE='\033[0;95m'
CYAN='\033[0;96m'
NC='\033[0m'
BOLD='\033[1m'

show_header() {
    clear
    echo -e "${RED}"
    cat << "EOF"
    ╔══════════════════════════════════════╗
    ║                                     ║
    ║              █████╗ ███████╗         ║
    ║             ██╔══██╗██╔════╝         ║
    ║             ███████║█████╗           ║
    ║             ██╔══██║██╔══╝           ║
    ║             ██║  ██║██║              ║
    ║             ╚═╝  ╚═╝╚═╝              ║
    ║                                     ║
    ╚══════════════════════════════════════╝
EOF
    echo -e "${NC}"
    echo -e "${CYAN}${BOLD}        ┌─────────────────────────┐${NC}"
    echo -e "${RED}${BOLD}              AF TOOL            ${NC}"
    echo -e "${CYAN}${BOLD}        └─────────────────────────┘${NC}"
    echo ""
}

log_message() {
    case $1 in
        "success") echo -e "${GREEN}${BOLD}✓ $2${NC}" ;;
        "error") echo -e "${RED}${BOLD}✗ $2${NC}" ;;
        "warning") echo -e "${YELLOW}${BOLD}⚠ $2${NC}" ;;
        "progress") echo -e "${PURPLE}${BOLD}⏳ $2${NC}" ;;
        "info") echo -e "${BLUE}${BOLD}➜ $2${NC}" ;;
        *) echo -e "${CYAN}${BOLD}● $2${NC}" ;;
    esac
}

check_termux() {
    [ ! -d "/data/data/com.termux/files/usr" ] && {
        log_message "error" "This script is designed for Termux only!"
        log_message "warning" "Please run this on Termux app"
        exit 1
    }
}

show_menu() {
    echo -e "${CYAN}${BOLD}"
    echo "┌─────────────────────────────────┐"
    echo "│        SELECT OPTION            │"
    echo "├─────────────────────────────────┤"
    echo "│  1. INSTALL ALL REQUIREMENTS    │"
    echo "│  2. RUN AF TOOL (SPAM SMS)      │"
    echo "│  3. TOOL INFO & DEVELOPER       │"
    echo "│  4. EXIT                        │"
    echo "└─────────────────────────────────┘"
    echo -e "${NC}"
    echo -n -e "${YELLOW}${BOLD}SELECT OPTION (1-4): ${NC}"
}

install_requirements() {
    log_message "progress" "Updating packages..."
    pkg update -y && pkg upgrade -y || {
        log_message "error" "Failed to update packages"
        return 1
    }

    log_message "progress" "Installing Python..."
    pkg install python -y || {
        log_message "error" "Failed to install Python"
        return 1
    }

    log_message "progress" "Installing PIP..."
    pkg install python-pip -y || {
        log_message "error" "Failed to install PIP"
        return 1
    }

    log_message "progress" "Installing requests library..."
    pip install requests || {
        log_message "error" "Failed to install requests"
        return 1
    }

    log_message "progress" "Installing git & curl..."
    pkg install git curl wget -y

    log_message "success" "Installation completed!"
    log_message "info" "Run: python3 afroto-tool.py"
    
    read -p "$(echo -e "${YELLOW}${BOLD}Run AF Tool now? (y/n): ${NC}")" -n 1
    echo
    [[ $REPLY =~ ^[Yy]$ ]] && python3 afroto-tool.py
}

run_af_tool() {
    [ -f "afroto-tool.py" ] && {
        log_message "progress" "Running AF Tool..."
        python3 afroto-tool.py
    } || {
        log_message "error" "AF Tool not found!"
        log_message "info" "Install requirements first (Option 1)"
    }
}

show_tool_info() {
    while true; do
        clear
        echo -e "${PURPLE}"
        echo "┌──────────────────────────────────────┐"
        echo "│         TOOL INFORMATION             │"
        echo "├──────────────────────────────────────┤"
        echo "│                                      │"
        echo -e "│   ${YELLOW}● Name: AF Tool${PURPLE}                        │"
        echo -e "│   ${YELLOW}● Version: 2.0${PURPLE}                         │"
        echo -e "│   ${YELLOW}● Function: Spam SMS${PURPLE}                   │"
        echo -e "│   ${YELLOW}● Developer: Afroto${PURPLE}                    │"
        echo "│                                      │"
        echo -e "│   ${GREEN}📞 WhatsApp: +201140184231${PURPLE}              │"
        echo -e "│   ${RED}📺 YouTube: @afroto${PURPLE}                       │"
        echo -e "│   ${BLUE}🌐 Website: afroto.com${PURPLE}                   │"
        echo "│                                      │"
        echo "└──────────────────────────────────────┘"
        echo -e "${NC}"
        
        echo -e "${YELLOW}${BOLD}Contact methods:${NC}"
        echo "1. 📞 WhatsApp"
        echo "2. 📺 YouTube" 
        echo "3. 🌐 Website"
        echo "4. 📢 Telegram"
        echo "5. ⬅️ Back"
        
        read -p "$(echo -e "${YELLOW}${BOLD}Choose (1-5): ${NC}")" -n 1
        echo
        
        case $REPLY in
            1) open_url "https://wa.me/201140184231" "Opening WhatsApp..." ;;
            2) open_url "https://youtube.com/@afroto" "Opening YouTube..." ;;
            3) open_url "https://afroto.com" "Opening Website..." ;;
            4) open_url "https://t.me/afroto" "Opening Telegram..." ;;
            5) break ;;
            *) log_message "error" "Invalid!" ;;
        esac
        
        [ "$REPLY" != "5" ] && read -p "$(echo -e "${YELLOW}Press Enter...${NC}")"
    done
}

open_url() {
    log_message "info" "$2"
    echo -e "${RED}🔗 $1${NC}"
    
    if command -v termux-open-url &> /dev/null; then
        termux-open-url "$1"
    elif command -v am &> /dev/null; then
        am start -a android.intent.action.VIEW -d "$1"
    else
        log_message "warning" "Cannot open automatically"
        log_message "info" "Visit: $1"
    fi
}

check_termux
show_header

while true; do
    show_menu
    read -r choice
    
    case $choice in
        1)
            echo -e "${RED}${BOLD}"
            echo "┌─────────────────────────────────┐"
            echo "│      INSTALLING REQUIREMENTS    │"
            echo "└─────────────────────────────────┘"
            echo -e "${NC}"
            install_requirements
            ;;
        2)
            echo -e "${RED}${BOLD}"
            echo "┌─────────────────────────────────┐"
            echo "│        RUNNING AF TOOL...       │"
            echo "└─────────────────────────────────┘"
            echo -e "${NC}"
            run_af_tool
            ;;
        3) show_tool_info ;;
        4)
            echo -e "${RED}${BOLD}"
            echo "┌─────────────────────────────────┐"
            echo "│           GOODBYE!              │"
            echo "└─────────────────────────────────┘"
            echo -e "${NC}"
            exit 0
            ;;
        *) log_message "error" "Invalid option! Choose 1-4" ;;
    esac
    
    echo
    read -p "$(echo -e "${YELLOW}${BOLD}Press Enter...${NC}")"
    show_header
done