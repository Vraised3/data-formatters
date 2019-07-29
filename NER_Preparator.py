import re

class Text_Label_Seperation:
	def __init__(self, filename, data_col_no, label_col_no):
		self.filename = filename
		self.data_col_no = data_col_no
		self.label_col_no = label_col_no
		self.sent_accumulator = []
		self.label_accumulator = []

	def data_labels_seperator(self):
		sent_accumulator = []
		label_accumulator = []
		with open(self.filename) as data:
			sent_words_accumulator = []
			sent_labels_accumulator = []
			for ind, line in enumerate(data):
				if line == '\n':
					self.sent_accumulator.append(sent_words_accumulator)
					self.label_accumulator.append(sent_labels_accumulator)
					sent_words_accumulator = []
					sent_labels_accumulator = []
				else:
					row_vals = re.split(r' ',line)
					try: # if any problems with indexing exists
						sent_words_accumulator.append(row_vals[self.data_col_no].strip('\n'))
						sent_labels_accumulator.append(row_vals[self.label_col_no].strip('\n'))
					except:
						raise Exception("Error on - Index: {}\tRow Values: {}".format(ind, row_vals))


	def vals_to_txt(self):
		file_words = open(self.filename.replace('.txt','') + '_words.txt', 'a+')
		file_labels = open(self.filename.replace('.txt','') + '_labels.txt', 'a+')
		for sent, labels in zip(self.sent_accumulator, self.label_accumulator):

			if(len(sent) != len(labels)):
				raise Exception('length mismatch of ', len(sent), len(labels))
			file_words.write(' '.join(sent) + '\n')
			file_labels.write(' '.join(labels) + '\n')

		file_words.close()
		file_labels.close()

	def prepare(self):
		self.data_labels_seperator()
		self.vals_to_txt()

if __name__ == '__main__':
	from NER_Preparator import Text_Label_Seperation
	prep = Text_Label_Seperation('train.txt', 0, 2)
	prep.prepare()
	prep = Text_Label_Seperation('test.txt', 0, 2)
	prep.prepare()

