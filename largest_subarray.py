class LargestSubArray:

    @staticmethod
    def get_length_of_longest_sub_array(l):
        """
        Given a list of integers, return the length of the longest sequence of ascending integers
        """
        if len(l) < 1:
            return 0

        longest_seen_sequence = 0

        this_sequence_length = 1

        previous = l[0]

        for _, current in enumerate(l):

            if current > previous:
                this_sequence_length = this_sequence_length + 1

                if this_sequence_length > longest_seen_sequence:
                    longest_seen_sequence = this_sequence_length

            else:
                this_sequence_length = 1

            if this_sequence_length > longest_seen_sequence:
                longest_seen_sequence = this_sequence_length

            previous = current

        return longest_seen_sequence

    def run(self):

        str_list = input("Enter the space delimited list of numbers\n")

        split_list = str_list.split(' ')

        input_list = []

        for s in split_list:
            input_list.append(int(s))

        length = self.get_length_of_longest_sub_array(input_list)

        print("Longest sequence of ascending numbers was {} elements long".format(length))
