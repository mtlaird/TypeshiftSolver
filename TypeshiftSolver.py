class TypeshiftBoard:

    def __init__(self):
        self.columns = []
        self.word_list = 'words'
        self.words = []
        self.combos = []
        self.valid_words = []

    def add_column(self, contents):
        if type(contents) is list:
            self.columns.append(contents)
        elif type(contents) is str:
            contents = contents.lower()
            self.columns.append(list(contents))

    def load_word_list(self):
        with open(self.word_list) as f:
            self.words = [line.rstrip('\n') for line in f]

    def get_combo(self, counter):
        ret_str = ''
        for i in range(len(counter)):
            ret_str += self.columns[i][counter[i]]

        return ret_str

    def iterate_counter(self, counter, iterate_col):
        if len(self.columns) > iterate_col:
            if len(self.columns[iterate_col]) > counter[iterate_col]+1:
                counter[iterate_col] += 1
                return counter, 0
            else:
                counter[iterate_col] = 0
                return self.iterate_counter(counter, iterate_col+1)
        else:
            return False, 0

    def generate_combinations(self):
        num_columns = len(self.columns)
        counter = [0] * num_columns
        iter_col = 0
        while counter:
            self.combos.append(self.get_combo(counter))
            counter, iter_col = self.iterate_counter(counter, iter_col)

    def solve(self):
        self.load_word_list()
        self.generate_combinations()
        for combo in self.combos:
            if combo in self.words:
                self.valid_words.append(combo)

    # This generates an incorrect board in some cases (if there is a blank between two characters)
    def board_html(self):
        html = "<table border=0>"
        for row in range(8):
            row_html = "<tr>"
            for col in range(8):
                try:
                    cell_value = self.columns[col][row]
                    row_html += "<td>" + cell_value + "</td>"
                except IndexError:
                    pass
            if row_html != "<tr>":
                row_html += "</tr>"
                html += row_html + "\n"
        html += "</table>\n"
        return html

    def valid_words_html(self):
        words = self.valid_words
        words.sort()
        html = ""
        last_start_letter = ""
        for word in words:
            if last_start_letter != "" and word[0] != last_start_letter:
                html += "<br>\n"
            html += word + " "
            last_start_letter = word[0]

        return html
