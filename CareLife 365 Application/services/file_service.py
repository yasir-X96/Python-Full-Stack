def write_data(filename, data):

    file = open(filename, "a")

    file.write(data + "\n")

    file.close()


def read_data(filename):

    file = open(filename, "r")

    records = file.readlines()

    file.close()

    return records