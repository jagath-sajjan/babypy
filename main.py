import babypy as easy

easy.say("Welcome to PyEasy Showcase!")

name = easy.ask("What's your name?")
age = easy.make_number(easy.ask("How old are you?"))

favorite_numbers = easy.make_list(7, 13, 42, 99)
easy.say(f"Favorite numbers: {favorite_numbers}")
easy.say(f"First: {easy.get_first(favorite_numbers)}, Last: {easy.get_last(favorite_numbers)}")

mixed_up = easy.mix_up(favorite_numbers)
easy.say(f"Mixed up: {mixed_up}")

lucky_number = easy.pick_random(favorite_numbers)
easy.say(f"Lucky number: {lucky_number}")

words = easy.split_big_word("Python is awesome and easy to learn")
easy.say(f"Words: {words}")
easy.say(f"Word count: {len(words)}")

sentence = easy.join_words(["You're", "awesome", name + "!"])
easy.say(sentence)

today = easy.get_today()
now = easy.get_now()
easy.say(f"Today: {today}, Time: {now}")

easy.wait_a_bit(2)

numbers = easy.count_from_to(1, 10)
even_numbers = easy.remove_copies([num for num in numbers if easy.is_even(num)])
odd_numbers = easy.remove_copies([num for num in numbers if easy.is_odd(num)])

easy.say(f"Even numbers: {even_numbers}")
easy.say(f"Odd numbers: {odd_numbers}")

person = easy.make_box(name=name, age=age, favorite_number=lucky_number)
easy.say(f"Person: {person}")
easy.say(f"Box labels: {list(person.keys())}")
easy.say(f"Box values: {list(person.values())}")

text = f"Hello, {name}!"
easy.say(f"Original: {text}")
easy.say(f"Loud: {easy.say_loudly(text)}")
easy.say(f"Quiet: {easy.say_quietly(text)}")
easy.say(f"Pretty: {easy.make_pretty(text)}")

numbers = easy.make_list(1, 2, 3, 4, 5)
easy.say(f"Numbers: {numbers}")
easy.say(f"Sum: {easy.add_up(numbers)}")
easy.say(f"Average: {easy.find_middle(numbers)}")

filename = "example.txt"
easy.write_file(filename, "Hello, PyEasy!")
easy.add_to_file(filename, " This is awesome!")
content = easy.read_file(filename)
easy.say(f"File content: {content}")

array = easy.make_array([1, 2, 3, 4, 5])
easy.say(f"Array: {array}")
easy.say(f"Array + 5: {easy.do_math(array, 5, '+')}")

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = easy.make_table(data)
easy.say(f"DataFrame:\n{df}")

easy.make_picture(numbers, [n**2 for n in numbers], "Square Numbers", "X", "Y^2")

easy.say(f"Max of numbers: {easy.get_max(numbers)}")
easy.say(f"Min of numbers: {easy.get_min(numbers)}")

easy.make_bar_chart(numbers, [n**2 for n in numbers], "Square Numbers", "X", "Y^2")
easy.make_scatter_plot(numbers, [n**2 for n in numbers], "Square Numbers", "X", "Y^2")

webpage = easy.get_webpage("https://example.com")
easy.say(f"Webpage content length: {easy.count_letters(webpage)}")

easy.say(f"Current directory contents: {easy.list_files('.')}")

easy.make_directory("test_dir")
easy.say("Created 'test_dir' directory")

easy.say(f"Random string: {easy.make_random_string(10)}")

easy.say(f"Factorial of 5: {easy.factorial(5)}")
easy.say(f"Is 17 prime? {easy.is_prime(17)}")

easy.say(f"IP Address: {easy.get_ip_address()}")

easy.say(f"System info: {easy.get_system_info()}")

stack = easy.Stack()
stack.push(1)
stack.push(2)
easy.say(f"Stack top: {stack.pop()}")

queue = easy.Queue()
queue.enqueue(1)
queue.enqueue(2)
easy.say(f"Queue front: {queue.dequeue()}")

easy.say(f"Fibonacci sequence: {easy.fibonacci(10)}")

easy.say(f"50% of 200 is: {easy.calculate_percentage(100, 200)}")

easy.say(f"Today is: {easy.get_day_of_week(easy.get_today())}")

easy.say(f"Word frequency in 'hello world': {easy.get_word_frequency('hello world hello')}")

easy.say(f"Longest word in 'Python is awesome': {easy.find_longest_word('Python is awesome')}")

easy.create_qr_code("https://example.com", "qr_code.png")
easy.say("QR code created: qr_code.png")

compressed = easy.compress_data("Hello, World!")
decompressed = easy.decompress_data(compressed)
easy.say(f"Compressed and decompressed: {decompressed}")

easy.say("That's all for now. Python is super easy with PyEasy!")