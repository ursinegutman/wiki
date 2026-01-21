#!/usr/bin/env bash

# Static Wiki Deployment Script
# Deploys the output directory to GitHub Pages

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="$PROJECT_ROOT/output"
DEPLOY_BRANCH="gh-pages"

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

# Check if output directory exists
check_output() {
    if [ ! -d "$OUTPUT_DIR" ]; then
        log_error "Output directory not found: $OUTPUT_DIR"
        log_info "Build the site first with:"
        echo ""
        echo "  ./scripts/build.sh"
        echo ""
        exit 1
    fi

    if [ -z "$(ls -A "$OUTPUT_DIR")" ]; then
        log_error "Output directory is empty: $OUTPUT_DIR"
        log_info "Build the site first with:"
        echo ""
        echo "  ./scripts/build.sh"
        echo ""
        exit 1
    fi

    log_info "Output directory found and is not empty."
}

# Check git status
check_git() {
    log_step "Checking git status..."

    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        log_error "Not a git repository"
        log_info "Initialize git first:"
        echo ""
        echo "  git init"
        echo "  git add ."
        echo "  git commit -m 'Initial commit'"
        echo ""
        exit 1
    fi

    # Check for uncommitted changes
    if ! git diff-index --quiet HEAD --; then
        log_warn "You have uncommitted changes"
        read -p "Continue anyway? (y/N) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            log_info "Deployment cancelled"
            exit 0
        fi
    fi

    log_info "Git repository is ready."
}

# Deploy to GitHub Pages
deploy() {
    log_step "Deploying to GitHub Pages..."
    echo ""

    log_info "This will deploy to the '$DEPLOY_BRANCH' branch"
    log_warn "The '$DEPLOY_BRANCH' branch will be replaced with the output directory contents"
    echo ""
    read -p "Continue? (y/N) " -n 1 -r
    echo

    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_info "Deployment cancelled"
        exit 0
    fi

    echo ""
    log_step "Creating deployment..."

    # Create a temporary directory
    local temp_dir=$(mktemp -d)

    # Copy output directory to temp
    cp -r "$OUTPUT_DIR"/* "$temp_dir/"

    # Initialize git in temp directory
    cd "$temp_dir"
    git init
    git add .
    git commit -m "Deploy to GitHub Pages"

    # Get the current branch
    cd "$PROJECT_ROOT"
    local current_branch=$(git branch --show-current)

    # Switch to deploy branch or create it
    if git show-ref --verify --quiet refs/heads/$DEPLOY_BRANCH; then
        git checkout $DEPLOY_BRANCH
        git rm -rf .
    else
        git checkout --orphan $DEPLOY_BRANCH
        git rm -rf .
    fi

    # Copy files from temp
    cp -r "$temp_dir"/* .
    git add .
    git commit -m "Deploy to GitHub Pages - $(date '+%Y-%m-%d %H:%M:%S')"

    # Push to remote
    if git remote get-url origin > /dev/null 2>&1; then
        log_step "Pushing to remote..."
        git push origin $DEPLOY_BRANCH --force
    else
        log_warn "No remote 'origin' found"
        log_info "Push manually with:"
        echo ""
        echo "  git push origin $DEPLOY_BRANCH --force"
        echo ""
    fi

    # Clean up temp directory
    rm -rf "$temp_dir"

    # Switch back to original branch
    git checkout $current_branch

    echo ""
    log_info "Deployment complete!"
    log_info "Your site should be live at:"
    echo ""
    echo "  https://<username>.github.io/<repository>/"
    echo ""
}

# Main
main() {
    log_info "========================================="
    log_info "  Static Wiki Deployment"
    log_info "========================================="
    echo ""

    log_info "Project root: $PROJECT_ROOT"
    log_info "Output directory: $OUTPUT_DIR"
    echo ""

    check_output
    check_git
    deploy
}

# Show usage
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Static Wiki Deployment Script"
    echo ""
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  --help, -h Show this help message"
    echo ""
    echo "This script deploys the output directory to GitHub Pages."
    echo ""
    echo "Setup:"
    echo "  1. Create a GitHub repository"
    echo "  2. Run: git remote add origin <repository-url>"
    echo "  3. Enable GitHub Pages in repository settings"
    echo "  4. Run this script"
    echo ""
    exit 0
fi

main
