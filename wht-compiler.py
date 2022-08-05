def open_file(path):
	file = open(path, 'r')
	content = file.read()
	lines = content.split('\n')
	compile(lines)


def create_file(content):
	file = open("test.html", "a")
	for line in content:
		file.write(line + '\n')
	file.close()
	file = open("test.html", "r")
	print(file.read())


def compile(lines):
	result = []
	for line in lines:
		compiled_line = handle_line(line)
		result.append(compiled_line)
	create_file(result)


def handle_line(line):
	if line:
		if all(char.isalpha() or char.isspace() for char in line):
			return line
		elif line[0] == '.':
			line = line[1:]
			strs = line.split()
			class_name = strs[0]
			rest = ''
			for str in strs[1:]:
				rest += ' '
				rest += str
			return '<p class="' + class_name + '">' +  rest + '</p>'
		elif line[0] == '#':
			size = line[1]
			header = '<h' + size + '>'
			closing = '</h' + size + '>'
			if '@' in line:
				link = handle_line(line[3:])
				return header + link + closing
			return header + closing
		elif line[0] == '@':
			line = line[1:]
			words = line.split()
			return '<a href="' + words[0] + '">' + words[1] + '</a>'
	match line:
		case '[':
			return '<span>'
		case ']':
			return '</span>'
		case '':
			return '<br>'


if __name__ == '__main__':
	import sys
	open_file(sys.argv[1])
