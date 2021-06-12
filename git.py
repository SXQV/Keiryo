# Import all the required modules
import os, sys

# Clear the screen
sys.stdout.write('\x1bc')

# Our main function
def main():
    sys.stdout.write('(\033[1;32mInfo\033[1;0m): Please enter your commit message\n')
    sys.stdout.write('(\033[1;32mInfo\033[1;0m): You can also enter \'exit\' or \'cancel\' to cancel\n')
    sys.stdout.write('(\033[1;32mInfo\033[1;0m): Commit message: ')
    commit_msg = input()

    # Check for the commit message
    # If it's `exit` or `cancel`, we abort the request
    # And exit
    if commit_msg.lower() == 'exit' or commit_msg.lower() == 'cancel':
        sys.stdout.write('(\033[1;32mInfo\033[1;0m): Aborting request...')
        sys.exit()

    # We add changes, commit them and push to remote
    os.system('git add .')
    os.system('git commit -q -m "{}"'.format(commit_msg))
    os.system('git push -q')

    # Once everything is done, we exit
    sys.exit()

if __name__ == '__main__':
    try:
        main()

    # Handle the `KeyboardInterrupt` error
    except KeyboardInterrupt:
        sys.stdout.write('\n(\033[1;31mError\033[1;0m): Keyboard interrupt\n')
        sys.stdout.write('(\033[1;31mError\033[1;0m): Aborting request...\n')

        try:
            sys.exit(0)

        # Handle the `SystemExit` error
        except SystemExit:
            os._exit(0)