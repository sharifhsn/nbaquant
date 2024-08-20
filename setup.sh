#!/bin/sh

# Function to check and install a command
install_if_not_exists() {
    command_name="$1"
    install_command="$2"

    if ! command -v "$command_name" >/dev/null 2>&1; then
        echo "'$command_name' command not found. Installing..."
        eval "$install_command"
    else
        echo "'$command_name' command is already installed."
    fi
}

# Install uv if not exists
install_if_not_exists "uv" "curl -LsSf https://astral.sh/uv/install.sh | sh"

# Install ruff if not exists
install_if_not_exists "ruff" "curl -LsSf https://astral.sh/uv/install.sh | sh"

# Ensure ~/.cargo/bin is in PATH
CARGO_BIN="$HOME/.cargo/bin"
case ":$PATH:" in
    *":$CARGO_BIN:"*) 
        # Path is already in PATH, do nothing
        ;;
    *)
        echo "Adding ~/.cargo/bin to PATH"
        export PATH="$CARGO_BIN:$PATH"

        # Detect shell and add to the appropriate shell profile
        case "$SHELL" in
            */zsh) SHELL_PROFILE="$HOME/.zshrc" ;;
            */bash) SHELL_PROFILE="$HOME/.bashrc" ;;
            */ksh) SHELL_PROFILE="$HOME/.kshrc" ;;
            */fish) SHELL_PROFILE="$HOME/.config/fish/config.fish" ;;
            *) SHELL_PROFILE="$HOME/.profile" ;;  # Default for other shells
        esac

        echo "export PATH=\"$CARGO_BIN:\$PATH\"" >> "$SHELL_PROFILE"
        echo "PATH updated in $SHELL_PROFILE. Please restart your shell or run: source $SHELL_PROFILE"
        ;;
esac
