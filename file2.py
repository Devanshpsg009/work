import csv
def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Rollno", "Student Name", "Marks"])
        writer.writerows(data)
        print(f"Data written to {filename} successfully.")
def read_from_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for i in reader:
            if i != [] or i != "":
                print(i)
                reader = csv.reader(file)
            else:
                print("End of File")
                break
def main():
    student_records = [
    ["101", "John Doe", "450"],
    ["102", "Jane Smith", "480"],
    ["103", "Bob Johnson", "420"],
    ]
    csv_filename = "students.csv"
    write_to_csv(csv_filename, student_records)
    read_from_csv(csv_filename)
if __name__ == "__main__":
    main()