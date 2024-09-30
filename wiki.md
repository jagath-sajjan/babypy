# Welcome to the BabyPy Wiki!

BabyPy is a user-friendly Python library that simplifies complex programming tasks. This wiki provides detailed documentation for all the functions available in BabyPy.

## Table of Contents

1. [Basic Operations](#basic-operations)
2. [Math and Statistics](#math-and-statistics)
3. [Date and Time](#date-and-time)
4. [File Operations](#file-operations)
5. [Data Structures](#data-structures)
6. [Data Analysis and Visualization](#data-analysis-and-visualization)
7. [Game Development](#game-development)
8. [Web Development and Scraping](#web-development-and-scraping)
9. [Database Operations](#database-operations)
10. [Network Operations](#network-operations)
11. [Encryption and Security](#encryption-and-security)
12. [System Operations](#system-operations)
13. [Audio Processing](#audio-processing)
14. [Machine Learning](#machine-learning)
15. [Natural Language Processing](#natural-language-processing)
16. [Image Processing](#image-processing)
17. [Computer Vision](#computer-vision)
18. [Geocoding](#geocoding)
19. [Text-to-Speech](#text-to-speech)
20. [QR Code Generation](#qr-code-generation)
21. [PDF Manipulation](#pdf-manipulation)
22. [Data Compression](#data-compression)

## Basic Operations

### say(words)
Print messages to the console.

**Parameters:**
- `words`: The message to print.

**Example:**
```python
say("Hello, World!")
```

### ask(question)
Get user input from the console.

**Parameters:**
- `question`: The prompt to display to the user.

**Returns:**
- The user's input as a string.

**Example:**
```python
name = ask("What's your name?")
```

### make_number(text)
Convert text to a number if possible.

**Parameters:**
- `text`: The text to convert.

**Returns:**
- An integer or float if conversion is successful, 0 otherwise.

**Example:**
```python
num = make_number("42")
```

### count_from_to(start, end)
Make a list of numbers from start to end.

**Parameters:**
- `start`: The starting number.
- `end`: The ending number (inclusive).

**Returns:**
- A list of numbers from start to end.

**Example:**
```python
numbers = count_from_to(1, 5)  # Returns [1, 2, 3, 4, 5]
```

### sort_stuff(things)
Put things in order.

**Parameters:**
- `things`: A list of items to sort.

**Returns:**
- A new sorted list.

**Example:**
```python
sorted_list = sort_stuff([3, 1, 4, 1, 5, 9, 2])
```

### mix_up(things)
Shuffle the order of things.

**Parameters:**
- `things`: A list of items to shuffle.

**Returns:**
- A new list with the items in random order.

**Example:**
```python
shuffled = mix_up([1, 2, 3, 4, 5])
```

### pick_random(things)
Choose one thing randomly.

**Parameters:**
- `things`: A list of items to choose from.

**Returns:**
- A randomly selected item from the list.

**Example:**
```python
chosen = pick_random(['apple', 'banana', 'cherry'])
```

### do_many_times(action, times)
Do something many times.

**Parameters:**
- `action`: A function to execute.
- `times`: The number of times to execute the function.

**Example:**
```python
do_many_times(lambda: say("Hello"), 3)
```

### make_list(*stuff)
Make a list of things.

**Parameters:**
- `*stuff`: Any number of items to put in the list.

**Returns:**
- A new list containing all the provided items.

**Example:**
```python
my_list = make_list(1, 2, 3, 'apple', 'banana')
```

### join_words(words)
Stick words together into one big word.

**Parameters:**
- `words`: A list of words to join.

**Returns:**
- A string with all words joined together.

**Example:**
```python
sentence = join_words(['Hello', 'world', '!'])
```

### split_big_word(big_word, by=" ")
Break a big word into smaller words.

**Parameters:**
- `big_word`: The string to split.
- `by`: The delimiter to split by (default is space).

**Returns:**
- A list of smaller words.

**Example:**
```python
words = split_big_word("Hello world!")
```

### get_first(things)
Get the first thing from a list.

**Parameters:**
- `things`: A list of items.

**Returns:**
- The first item in the list, or None if the list is empty.

**Example:**
```python
first = get_first([1, 2, 3])
```

### get_last(things)
Get the last thing from a list.

**Parameters:**
- `things`: A list of items.

**Returns:**
- The last item in the list, or None if the list is empty.

**Example:**
```python
last = get_last([1, 2, 3])
```

### remove_copies(things)
Keep only one of each thing.

**Parameters:**
- `things`: A list of items, possibly with duplicates.

**Returns:**
- A new list with duplicates removed.

**Example:**
```python
unique = remove_copies([1, 2, 2, 3, 3, 3])
```

### count_things(things)
Count how many of each thing there are.

**Parameters:**
- `things`: A list of items.

**Returns:**
- A dictionary with items as keys and their counts as values.

**Example:**
```python
counts = count_things(['apple', 'banana', 'apple', 'cherry'])
```

### is_inside(item, things)
Check if something is in a group of things.

**Parameters:**
- `item`: The item to search for.
- `things`: The list to search in.

**Returns:**
- True if the item is in the list, False otherwise.

**Example:**
```python
found = is_inside('apple', ['banana', 'apple', 'cherry'])
```

### add_lists(*lists)
Put many lists together into one big list.

**Parameters:**
- `*lists`: Any number of lists to combine.

**Returns:**
- A new list containing all items from all provided lists.

**Example:**
```python
big_list = add_lists([1, 2], [3, 4], [5, 6])
```

### flip_order(things)
Reverse the order of things.

**Parameters:**
- `things`: A list of items.

**Returns:**
- A new list with the items in reverse order.

**Example:**
```python
reversed_list = flip_order([1, 2, 3, 4, 5])
```

## Math and Statistics

### add_up(numbers)
Add up all the numbers in a list.

**Parameters:**
- `numbers`: A list of numbers.

**Returns:**
- The sum of all numbers in the list.

**Example:**
```python
total = add_up([1, 2, 3, 4, 5])
```

### find_middle(numbers)
Find the average of a list of numbers.

**Parameters:**
- `numbers`: A list of numbers.

**Returns:**
- The average of the numbers.

**Example:**
```python
average = find_middle([1, 2, 3, 4, 5])
```

### make_rounder(number, decimals=0)
Round a number to a certain number of decimal places.

**Parameters:**
- `number`: The number to round.
- `decimals`: The number of decimal places to round to (default is 0).

**Returns:**
- The rounded number.

**Example:**
```python
rounded = make_rounder(3.14159, decimals=2)
```

### factorial(n)
Calculate the factorial of a number.

**Parameters:**
- `n`: The number to calculate the factorial of.

**Returns:**
- The factorial of n.

**Example:**
```python
fact = factorial(5)  # Returns 120
```

### is_prime(n)
Check if a number is prime.

**Parameters:**
- `n`: The number to check.

**Returns:**
- True if the number is prime, False otherwise.

**Example:**
```python
is_prime_num = is_prime(17)  # Returns True
```

### fibonacci(n)
Generate a Fibonacci sequence of length n.

**Parameters:**
- `n`: The length of the Fibonacci sequence to generate.

**Returns:**
- A list containing the Fibonacci sequence.

**Example:**
```python
fib_seq = fibonacci(10)  # Returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### calculate_percentage(part, whole)
Calculate what percentage part is of whole.

**Parameters:**
- `part`: The part value.
- `whole`: The whole value.

**Returns:**
- The percentage as a float.

**Example:**
```python
percentage = calculate_percentage(25, 100)  # Returns 25.0
```

## Date and Time

### get_today()
Get the current date.

**Returns:**
- A datetime.date object representing today's date.

**Example:**
```python
today = get_today()
```

### get_now()
Get the current time.

**Returns:**
- A datetime.time object representing the current time.

**Example:**
```python
current_time = get_now()
```

### wait_a_bit(seconds)
Wait for a little while.

**Parameters:**
- `seconds`: The number of seconds to wait.

**Example:**
```python
wait_a_bit(5)  # Waits for 5 seconds
```

### format_date(date, format_string)
Format a date according to the given format string.

**Parameters:**
- `date`: A datetime.date object.
- `format_string`: A string specifying the desired format.

**Returns:**
- A formatted date string.

**Example:**
```python
formatted = format_date(get_today(), "%Y-%m-%d")
```

### date_difference(date1, date2)
Calculate the difference between two dates.

**Parameters:**
- `date1`: The first date.
- `date2`: The second date.

**Returns:**
- The number of days between the two dates.

**Example:**
```python
diff = date_difference(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))
```

### get_day_of_week(date)
Get the day of the week for a given date.

**Parameters:**
- `date`: A datetime.date object.

**Returns:**
- The name of the day of the week.

**Example:**
```python
day = get_day_of_week(datetime.date(2023, 5, 1))  # Returns "Monday"
```

### add_days_to_date(date, days)
Add a number of days to a date.

**Parameters:**
- `date`: A datetime.date object.
- `days`: The number of days to add.

**Returns:**
- A new datetime.date object.

**Example:**
```python
new_date = add_days_to_date(datetime.date(2023, 1, 1), 30)
```

## File Operations

### read_file(filename)
Read what's inside a file.

**Parameters:**
- `filename`: The name of the file to read.

**Returns:**
- The contents of the file as a string.

**Example:**
```python
content = read_file("example.txt")
```

### write_file(filename, stuff)
Write stuff into a file.

**Parameters:**
- `filename`: The name of the file to write to.
- `stuff`: The content to write to the file.

**Example:**
```python
write_file("example.txt", "Hello, world!")
```

### add_to_file(filename, stuff)
Add more stuff to the end of a file.

**Parameters:**
- `filename`: The name of the file to append to.
- `stuff`: The content to append to the file.

**Example:**
```python
add_to_file("example.txt", "\nThis is a new line.")
```

### list_files(directory)
List all files in a directory.

**Parameters:**
- `directory`: The path to the directory.

**Returns:**
- A list of filenames in the directory.

**Example:**
```python
files = list_files("/path/to/directory")
```

### make_directory(directory)
Create a new directory.

**Parameters:**
- `directory`: The path of the directory to create.

**Example:**
```python
make_directory("/path/to/new_directory")
```

### delete_file(filename)
Delete a file.

**Parameters:**
- `filename`: The name of the file to delete.

**Example:**
```python
delete_file("unwanted_file.txt")
```

### get_file_size(filename)
Get the size of a file in bytes.

**Parameters:**
- `filename`: The name of the file.

**Returns:**
- The size of the file in bytes.

**Example:**
```python
size = get_file_size("example.txt")
```

### rename_file(old_name, new_name)
Rename a file.

**Parameters:**
- `old_name`: The current name of the file.
- `new_name`: The new name for the file.

**Example:**
```python
rename_file("old_file.txt", "new_file.txt")
```

### count_lines_in_file(filename)
Count the number of lines in a file.

**Parameters:**
- `filename`: The name of the file.

**Returns:**
- The number of lines in the file.

**Example:**
```python
line_count = count_lines_in_file("example.txt")
```

### find_files_by_extension(directory, extension)
Find all files with a specific extension in a directory.

**Parameters:**
- `directory`: The path to the directory to search.
- `extension`: The file extension to search for.

**Returns:**
- A list of filenames with the specified extension.

**Example:**
```python
python_files = find_files_by_extension("/path/to/directory", ".py")
```

## Data Structures

### make_box(**stuff)
Make a box (dictionary) and put stuff in it with labels.

**Parameters:**
- `**stuff`: Keyword arguments to add to the dictionary.

**Returns:**
- A new dictionary with the provided key-value pairs.

**Example:**
```python
box = make_box(name="Alice", age=30, city="New York")
```

### Stack
A simple implementation of a stack data structure.

**Methods:**
- `push(item)`: Add an item to the top of the stack.
- `pop()`: Remove and return the top item from the stack.
- `is_empty()`: Check if the stack is empty.

**Example:**
```python
stack = Stack()
stack.push(1)
stack.push(2)
top_item = stack.pop()
```

### Queue
A simple implementation of a queue data structure.

**Methods:**
- `enqueue(item)`: Add an item to the end of the queue.
- `dequeue()`: Remove and return the first item from the queue.
- `is_empty()`: Check if the queue is empty.

**Example:**
```python
queue = Queue()
queue.enqueue("first")
queue.enqueue("second")
first_item = queue.dequeue()
```

### PriorityQueue
A simple implementation of a priority queue data structure.

**Methods:**
- `enqueue(item, priority)`: Add an item with a given priority to the queue.
- `dequeue()`: Remove and return the item with the highest priority.

**Example:**
```python
pq = PriorityQueue()
pq.enqueue("important", 2)
pq.enqueue("very important", 1)
highest_priority_item = pq.dequeue()
```

## Data Analysis and Visualization

### make_table(data)
Make a table (DataFrame) from a dictionary or list.

**Parameters:**
- `data`: A dictionary or list of data.

**Returns:**
- A pandas DataFrame.

**Example:**
```python
table = make_table({"Name": ["Alice", "Bob"], "Age": [30, 25]})
```

### read_csv(filename)
Read a CSV file into a table.

**Parameters:**
- `filename`: The name of the CSV file.

**Returns:**
- A pandas DataFrame containing the CSV data.

**Example:**
```python
df = read_csv("data.csv")
```

### save_csv(table, filename)
Save a table to a CSV file.

**Parameters:**
- `table`: A pandas DataFrame to save.
- `filename`: The name of the file to save to.

**Example:**
```python
save_csv(df, "output.csv")
```

### make_picture(x, y, title="My Picture", x_label="X", y_label="Y")
Draw a picture (plot) with numbers.

**Parameters:**
- `x`: Data for the x-axis.
- `y`: Data for the y-axis.
- `title`: The title of the plot (default: "My Picture").
- `x_label`: The label for the x-axis (default: "X").
- `y_label`: The label for the y-axis (default: "Y").

**Example:**
```python
make_picture([1, 2, 3], [4, 5, 6], title="My Line Plot")
```

### make_bar_chart(x, y, title="Bar Chart", x_label="X", y_label="Y")
Create a bar chart.

**Parameters:**
- `x`: Categories for the x-axis.
- `y`: Values for the y-axis.
- `title`: The title of the chart (default: "Bar Chart").
- `x_label`: The label for the x-axis (default: "X").
- `y_label`: The label for the y-axis (default: "Y").

**Example:**
```python
make_bar_chart(["A", "B", "C"], [1, 2, 3], title="My Bar Chart")
```

### make_scatter_plot(x, y, title="Scatter Plot", x_label="X", y_label="Y")
Create a scatter plot.

**Parameters:**
- `x`: Data for the x-axis.
- `y`: Data for the y-axis.
- `title`: The title of the plot (default: "Scatter Plot").
- `x_label`: The label for the x-axis (default: "X").
- `y_label`: The label for the y-axis (default: "Y").

**Example:**
```python
make_scatter_plot([1, 2, 3, 4], [1, 4, 9, 16], title="My Scatter Plot")
```

### save_picture(filename)
Save the current plot to a file.

**Parameters:**
- `filename`: The name of the file to save the plot to.

**Example:**
```python
save_picture("my_plot.png")
```

### make_heatmap(data, title="Heatmap", x_label="X", y_label="Y")
Create a heatmap.

**Parameters:**
- `data`: A 2D array of data.
- `title`: The title of the heatmap (default: "Heatmap").
- `x_label`: The label for the x-axis (default: "X").
- `y_label`: The label for the y-axis (default: "Y").

**Example:**
```python
make_heatmap([[1, 2, 3], [4, 5, 6], [7, 8, 9]], title="My Heatmap")
```

## Game Development

### start_game(width=800, height=600, title="My Game")
Start a new game window.

**Parameters:**
- `width`: The width of the game window (default: 800).
- `height`: The height of the game window (default: 600).
- `title`: The title of the game window (default: "My Game").

**Returns:**
- A pygame screen object.

**Example:**
```python
screen = start_game(width=1024, height=768, title="My Awesome Game")
```

### draw_circle(screen, color, position, radius)
Draw a circle in the game.

**Parameters:**
- `screen`: The pygame screen to draw on.
- `color`: The color of the circle (as an RGB tuple).
- `position`: The (x, y) position of the circle's center.
- `radius`: The radius of the circle.

**Example:**
```python
draw_circle(screen, (255, 0, 0), (100, 100), 50)
```

### draw_rectangle(screen, color, position, size)
Draw a rectangle in the game.

**Parameters:**
- `screen`: The pygame screen to draw on.
- `color`: The color of the rectangle (as an RGB tuple).
- `position`: The (x, y) position of the top-left corner of the rectangle.
- `size`: The (width, height) of the rectangle.

**Example:**
```python
draw_rectangle(screen, (0, 255, 0), (200, 200), (100, 50))
```

### update_game()
Update the game display.

**Example:**
```python
update_game()
```

### end_game()
End the game.

**Example:**
```python
end_game()
```

### load_image(filename)
Load an image for use in the game.

**Parameters:**
- `filename`: The name of the image file to load.

**Returns:**
- A pygame image object.

**Example:**
```python
player_image = load_image("player.png")
```

### draw_image(screen, image, position)
Draw an image on the game screen.

**Parameters:**
- `screen`: The pygame screen to draw on.
- `image`: The pygame image object to draw.
- `position`: The (x, y) position to draw the image at.

**Example:**
```python
draw_image(screen, player_image, (100, 100))
```

### get_key_pressed()
Get the current pressed key.

**Returns:**
- A dictionary-like object representing the state of all keyboard buttons.

**Example:**
```python
keys = get_key_pressed()
if keys[pygame.K_SPACE]:
    print("Space bar is pressed!")
```

### make_sound(filename)
Create a sound object from a file.

**Parameters:**
- `filename`: The name of the sound file to load.

**Returns:**
- A pygame sound object.

**Example:**
```python
jump_sound = make_sound("jump.wav")
```

### play_sound(sound)
Play a sound.

**Parameters:**
- `sound`: The pygame sound object to play.

**Example:**
```python
play_sound(jump_sound)
```

### create_sprite(image_path, x, y)
Create a simple sprite for Pygame.

**Parameters:**
- `image_path`: The file path to the sprite's image.
- `x`: The initial x-coordinate of the sprite.
- `y`: The initial y-coordinate of the sprite.

**Returns:**
- A pygame sprite object.

**Example:**
```python
player_sprite = create_sprite("player.png", 100, 100)
```

### detect_collision(sprite1, sprite2)
Detect collision between two sprites.

**Parameters:**
- `sprite1`: The first sprite to check for collision.
- `sprite2`: The second sprite to check for collision.

**Returns:**
- True if the sprites are colliding, False otherwise.

**Example:**
```python
if detect_collision(player_sprite, enemy_sprite):
    print("Collision detected!")
```

## Web Development and Scraping

### get_webpage(url)
Get the content of a webpage.

**Parameters:**
- `url`: The URL of the webpage to fetch.

**Returns:**
- The HTML content of the webpage as a string.

**Example:**
```python
content = get_webpage("https://www.example.com")
```

### download_file(url, filename)
Download a file from a URL.

**Parameters:**
- `url`: The URL of the file to download.
- `filename`: The name to save the downloaded file as.

**Example:**
```python
download_file("https://example.com/image.jpg", "downloaded_image.jpg")
```

### parse_html(html)
Parse HTML content.

**Parameters:**
- `html`: The HTML content to parse.

**Returns:**
- A BeautifulSoup object representing the parsed HTML.

**Example:**
```python
soup = parse_html(content)
```

### find_all_tags(soup, tag)
Find all occurrences of a specific tag in parsed HTML.

**Parameters:**
- `soup`: A BeautifulSoup object containing parsed HTML.
- `tag`: The HTML tag to search for.

**Returns:**
- A list of all matching tags.

**Example:**
```python
links = find_all_tags(soup, 'a')
```

### run_web_server(host='0.0.0.0', port=5000)
Run a simple web server.

**Parameters:**
- `host`: The host to run the server on (default: '0.0.0.0').
- `port`: The port to run the server on (default: 5000).

**Example:**
```python
run_web_server()
```

### scrape_dynamic_content(url, element_id, timeout=10)
Scrape content from a dynamic website.

**Parameters:**
- `url`: The URL of the dynamic website.
- `element_id`: The ID of the element to wait for and scrape.
- `timeout`: The maximum time to wait for the element (default: 10 seconds).

**Returns:**
- The text content of the specified element.

**Example:**
```python
content = scrape_dynamic_content("https://example.com", "dynamic-content")
```

### get_all_links(url)
Get all links from a webpage.

**Parameters:**
- `url`: The URL of the webpage to scrape links from.

**Returns:**
- A list of all href values found in the webpage.

**Example:**
```python
links = get_all_links("https://www.example.com")
```

### download_image(url, filename)
Download an image from a URL.

**Parameters:**
- `url`: The URL of the image to download.
- `filename`: The name to save the downloaded image as.

**Example:**
```python
download_image("https://example.com/image.jpg", "downloaded_image.jpg")
```

## Database Operations

### connect_to_db(db_name)
Connect to a SQLite database.

**Parameters:**
- `db_name`: The name of the database file.

**Returns:**
- A database connection object.

**Example:**
```python
conn = connect_to_db("my_database.db")
```

### run_query(connection, query)
Run a SQL query on the database.

**Parameters:**
- `connection`: A database connection object.
- `query`: The SQL query to execute.

**Returns:**
- The results of the query as a list of tuples.

**Example:**
```python
results = run_query(conn, "SELECT * FROM users")
```

### close_db(connection)
Close the database connection.

**Parameters:**
- `connection`: The database connection to close.

**Example:**
```python
close_db(conn)
```

## Network Operations

### get_ip_address()
Get the machine's IP address.

**Returns:**
- The IP address as a string.

**Example:**
```python
ip = get_ip_address()
```

### ping_address(address)
Ping an IP address or domain.

**Parameters:**
- `address`: The IP address or domain to ping.

**Returns:**
- True if the ping was successful, False otherwise.

**Example:**
```python
is_reachable = ping_address("www.example.com")
```

### get_public_ip()
Get the public IP address.

**Returns:**
- The public IP address as a string.

**Example:**
```python
public_ip = get_public_ip()
```

### is_port_open(host, port)
Check if a port is open on a given host.

**Parameters:**
- `host`: The host to check.
- `port`: The port number to check.

**Returns:**
- True if the port is open, False otherwise.

**Example:**
```python
is_open = is_port_open("example.com", 80)
```

These functions provide basic network operations, allowing users to retrieve IP addresses, ping hosts, and check for open ports. This simplifies network-related tasks for beginners while still providing essential functionality.

## Encryption and Security

### make_hash(text)
Create a hash of the given text.

**Parameters:**
- `text`: The text to hash.

**Returns:**
- The hash of the text as a hexadecimal string.

**Example:**
```python
hash_value = make_hash("Hello, World!")
```

## System Operations

### get_system_info()
Get basic system information.

**Returns:**
- A dictionary containing system information.

**Example:**
```python
info = get_system_info()
print(f"Operating System: {info['system']}")
print(f"Version: {info['version']}")
print(f"Machine: {info['machine']}")
```

## Audio Processing

### record_audio(filename, duration=5, sample_rate=44100, channels=2, chunk=1024)
Record audio for a specified duration.

**Parameters:**
- `filename`: The name of the file to save the recording.
- `duration`: The duration of the recording in seconds (default: 5).
- `sample_rate`: The sample rate of the recording (default: 44100).
- `channels`: The number of audio channels (default: 2).
- `chunk`: The size of audio chunks to process (default: 1024).

**Example:**
```python
record_audio("my_recording.wav", duration=10)
```

## Machine Learning

### simple_linear_regression(X, y)
Perform simple linear regression.

**Parameters:**
- `X`: The input features (independent variables).
- `y`: The target values (dependent variable).

**Returns:**
- A tuple containing the trained model and the mean squared error.

**Example:**
```python
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 5, 4, 5]
model, mse = simple_linear_regression(X, y)
print(f"Mean Squared Error: {mse}")
```

## Natural Language Processing

### tokenize_text(text)
Tokenize text into words.

**Parameters:**
- `text`: The text to tokenize.

**Returns:**
- A list of tokens (words).

**Example:**
```python

## Image Processing

### open_image(filename)
Open an image file.

**Parameters:**
- `filename`: The name of the image file to open.

**Returns:**
- A PIL Image object.

**Example:**
```python
image = open_image("example.jpg")
```

### save_image(image, filename)
Save an image to a file.

**Parameters:**
- `image`: The PIL Image object to save.
- `filename`: The name of the file to save the image as.

**Example:**
```python
save_image(image, "saved_image.jpg")
```

### resize_image(image, size)
Resize an image.

**Parameters:**
- `image`: The PIL Image object to resize.
- `size`: A tuple containing the new (width, height) of the image.

**Returns:**
- A new PIL Image object with the specified size.

**Example:**
```python
resized_image = resize_image(image, (300, 200))
```

### rotate_image(image, degrees)
Rotate an image.

**Parameters:**
- `image`: The PIL Image object to rotate.
- `degrees`: The number of degrees to rotate the image.

**Returns:**
- A new PIL Image object that has been rotated.

**Example:**
```python
rotated_image = rotate_image(image, 90)
```

### apply_filter(image, filter_name)
Apply a filter to an image.

**Parameters:**
- `image`: The PIL Image object to apply the filter to.
- `filter_name`: The name of the filter to apply. Can be 'blur', 'sharpen', or 'emboss'.

**Returns:**
- A new PIL Image object with the filter applied.

**Example:**
```python
blurred_image = apply_filter(image, 'blur')
```

### crop_image(image, box)
Crop an image to a specific region.

**Parameters:**
- `image`: The PIL Image object to crop.
- `box`: A tuple defining the region to crop (left, upper, right, lower).

**Returns:**
- A new PIL Image object that has been cropped.

**Example:**
```python
cropped_image = crop_image(image, (100, 100, 300, 300))
```

## Computer Vision

### capture_image(camera=0)
Capture an image from the camera.

**Parameters:**
- `camera`: The index of the camera to use (default is 0 for the primary camera).

**Returns:**
- A numpy array representing the captured image.

**Example:**
```python
frame = capture_image()
```

### save_image_cv2(image, filename)
Save an image using OpenCV.

**Parameters:**
- `image`: The numpy array representing the image to save.
- `filename`: The name of the file to save the image as.

**Example:**
```python
save_image_cv2(frame, "captured_image.jpg")
```

These functions provide basic image processing and computer vision capabilities using the PIL (Python Imaging Library) and OpenCV libraries. They allow users to open, save, resize, rotate, and apply filters to images, as well as capture images from a camera. These operations are commonly used in various image processing and computer vision tasks.

## Geocoding

### get_coordinates(address)
Get latitude and longitude for an address.

**Parameters:**
- `address`: The address to geocode.

**Returns:**
- A tuple containing (latitude, longitude) if the address is found, or None if not found.

**Example:**
```python
coords = get_coordinates("1600 Amphitheatre Parkway, Mountain View, CA")
if coords:
    print(f"Latitude: {coords[0]}, Longitude: {coords[1]}")
else:
    print("Address not found")
```

## Text-to-Speech

### text_to_speech(text)
Convert text to speech and play it.

**Parameters:**
- `text`: The text to convert to speech.

**Example:**
```python
text_to_speech("Hello, world! This is BabyPy speaking.")
```

This function uses the pyttsx3 library to convert text to speech and play it through the default audio output device. It doesn't return any value but produces audible speech output.

## QR Code Generation

### create_qr_code(data, filename)
Create a QR code and save it to a file.

**Parameters:**
- `data`: The data to encode in the QR code.
- `filename`: The name of the file to save the QR code image as.

**Example:**
```python
create_qr_code("https://example.com", "my_qr_code.png")
```

This function creates a QR code containing the specified data and saves it as an image file. The QR code is generated with a version 1 format, a box size of 10, and a border of 5 units. The resulting image has a black foreground on a white background.

## PDF Manipulation

### merge_pdfs(pdf_files, output_filename)
Merge multiple PDF files into one.

**Parameters:**
- `pdf_files`: A list of filenames or file paths of the PDF files to merge.
- `output_filename`: The name of the file to save the merged PDF as.

**Example:**
```python
merge_pdfs(["file1.pdf", "file2.pdf", "file3.pdf"], "merged_output.pdf")
```

This function takes multiple PDF files and combines them into a single PDF file. The PDFs are merged in the order they are provided in the `pdf_files` list. Each page from each input PDF is added to the output PDF in sequence.

Note: This function uses the PyPDF2 library, which may have limitations with certain types of PDF files, especially those with complex formatting or security features.

## Data Compression

### compress_data(data)
Compress data using zlib.

**Parameters:**
- `data`: The string data to compress.

**Returns:**
- Compressed data as bytes.

**Example:**
```python
compressed = compress_data("Hello, World!")
```

### decompress_data(compressed_data)
Decompress data using zlib.

**Parameters:**
- `compressed_data`: The compressed data to decompress.

**Returns:**
- The decompressed data as a string.

**Example:**
```python
original = decompress_data(compressed)
```

This concludes the documentation for the BabyPy module. Each function is designed to simplify complex programming tasks, making Python more accessible to beginners and more efficient for experienced developers.
