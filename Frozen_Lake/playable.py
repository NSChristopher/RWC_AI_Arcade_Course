import gymnasium as gym
import curses

# Define action mapping for arrow keys
key_mapping = {
    curses.KEY_LEFT: 0,   # Move left
    curses.KEY_DOWN: 1,   # Move down
    curses.KEY_RIGHT: 2,  # Move right
    curses.KEY_UP: 3      # Move up
}

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Initialize the FrozenLake environment
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    env.reset()

    stdscr.addstr(0, 0, "FrozenLake-v1 Environment")
    stdscr.addstr(1, 0, "Use the arrow keys to control the agent:")
    stdscr.refresh()

    # Render the initial state
    env.render()

    while True:
        # Get user input
        key = stdscr.getch()

        if key in key_mapping:
            # Perform the action
            action = key_mapping[key]
            state, reward, done, _, _ = env.step(action)

            # Clear the screen
            stdscr.clear()

            # Render the new state
            env.render()

            # Display messages
            stdscr.addstr(0, 0, "FrozenLake-v1 Environment")
            stdscr.addstr(1, 0, "Use the arrow keys to control the agent:")

            if done:
                if reward == 1:
                    stdscr.addstr(2, 0, "Congratulations! You've reached the goal.")
                else:
                    stdscr.addstr(2, 0, "You fell into a hole.")
                stdscr.refresh()
                break

        stdscr.refresh()

    # Close the environment
    env.close()

# Run the main function within curses wrapper
curses.wrapper(main)
