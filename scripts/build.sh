#!/usr/bin/env bash

# Static Wiki Builder with Tyrian Theme
# This script builds the static site from markdown files

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
PYTHON_SCRIPT="$SCRIPT_DIR/markdown2html.py"

# Functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_step() {
    echo -e "${BLUE}[STEP]${NC} $1"
}

# Check if Python is available
check_python() {
    if ! command -v python3 &> /dev/null; then
        log_error "Python 3 is not installed"
        log_info "Install Python from: https://www.python.org/downloads/"
        exit 1
    fi
    log_info "Python found: $(python3 --version)"
}

# Check Python dependencies
check_dependencies() {
    log_step "Checking Python dependencies..."

    local missing_deps=()

    for dep in markdown pystache frontmatter; do
        if ! python3 -c "import ${dep}" 2>/dev/null; then
            case $dep in
                frontmatter)
                    missing_deps+=("python-frontmatter")
                    ;;
                *)
                    missing_deps+=("$dep")
                    ;;
            esac
        fi
    done

    if [ ${#missing_deps[@]} -gt 0 ]; then
        log_error "Missing Python dependencies: ${missing_deps[*]}"
        log_info "Install them with:"
        echo ""
        echo "  pip install ${missing_deps[*]}"
        echo ""
        log_info "Or using requirements.txt:"
        echo ""
        echo "  pip install -r requirements.txt"
        exit 1
    fi

    log_info "All Python dependencies are installed."
}

# Check if Tyrian theme is installed
check_theme() {
    log_step "Checking Tyrian theme installation..."

    local theme_path="$PROJECT_ROOT/node_modules/@gentoo/tyrian"

    if [ ! -d "$theme_path" ]; then
        log_error "Tyrian theme not found at: $theme_path"
        log_info "Install it with:"
        echo ""
        echo "  npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git"
        echo ""
        exit 1
    fi

    log_info "Tyrian theme found."
}

# Main build process
main() {
    log_info "========================================="
    log_info "  Static Wiki Builder"
    log_info "  Powered by Tyrian Theme"
    log_info "========================================="
    echo ""

    log_info "Project root: $PROJECT_ROOT"
    echo ""

    # Run checks
    check_python
    check_dependencies
    check_theme

    echo ""
    log_step "Building static site..."
    echo ""

    # Change to project root directory
    cd "$PROJECT_ROOT"

    # Run Python build script
    if [ "$1" == "--clean" ]; then
        log_info "Clean build requested."
        python3 "$PYTHON_SCRIPT" --clean
    else
        python3 "$PYTHON_SCRIPT"
    fi

    local exit_code=$?

    echo ""
    if [ $exit_code -eq 0 ]; then
        log_info "========================================="
        log_info "  Build completed successfully!"
        log_info "========================================="
        echo ""
        log_info "Output directory: $PROJECT_ROOT/output"
        echo ""
        log_info "To preview the site:"
        echo ""
        echo "  cd $PROJECT_ROOT/output"
        echo "  python3 -m http.server 8000"
        echo ""
        echo "Then visit: http://localhost:8000"
        echo ""
        log_info "To deploy to GitHub Pages:"
        echo ""
        echo "  ./scripts/deploy.sh"
        echo ""
    else
        log_error "Build failed with exit code: $exit_code"
        exit $exit_code
    fi
}

# Show usage if help is requested
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Static Wiki Builder - Build Script"
    echo ""
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  --clean    Clean output directory before building"
    echo "  --help, -h Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0              # Build the site"
    echo "  $0 --clean      # Clean build"
    echo ""
    exit 0
fi

# Run main function
main "$@"
