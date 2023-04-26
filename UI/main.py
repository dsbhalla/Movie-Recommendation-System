#Imports
import csv
import tkinter
from tkinter import ttk, END, PhotoImage

#User Recommendation Search Section
file = open('user_recommedations.csv')

csvreader = csv.reader(file, delimiter=',', quotechar='"')
data = {}

#For loops to read data
for i in range (611):
    data[str(i)] = []

for row in csvreader:
    data[row[0]].append(row)

#Movies Recommendation Search Section
file = open('similar_movies.csv', encoding="utf8")

#Read Data from CSV
csvreader = csv.reader(file, delimiter=',', quotechar='"')
dataMovie = {}

#Loops to Comb Through CSV
for i in range (193610):
    dataMovie[str(i)] = []

key = ""
for i, row in enumerate(csvreader):
    if i % 21 == 0:
        key = row[0]

    dataMovie[key].append(row)

#Genre Recommendation Search Section
file = open('movies_by_genre.csv', encoding="utf8")

#Read through CSV
csvreader = csv.reader(file, delimiter=',', quotechar='"')
dataGenre = {}
genres = ['Animation', 'Mystery', 'Romance', 'Film-Noir', 'Crime', 'Musical', 
          'IMAX', 'Horror', 'Adventure', 'Action', 'War', 'Drama', 'Sci-Fi', 'Western', 'Children', 'Documentary', 'Comedy', 'Thriller', 'Fantasy', 'genre']

#Loops to get the data formatted
for i in genres:
    dataGenre[i] = []

for row in csvreader:
    dataGenre[row[4]].append(row[:-2])



#Display Functions User
def display_recommendations_user():
    for widget in test_frame.winfo_children():
        widget.destroy()

    userID = userId_entry.get()
    numberOfResults = int(numberOfResults_spinbox.get())

    idLabel = tkinter.Label(test_frame, text="User ID")
    idLabel.grid(row=0, column=0)
    movieLabel = tkinter.Label(test_frame, text="Movie Name")
    movieLabel.grid(row=0, column=1)
    ratingLabel = tkinter.Label(test_frame, text="Rating")
    ratingLabel.grid(row=0, column=2)
    
    for i in range(1, numberOfResults+1):
            for j in range(3):
                d = tkinter.Entry(test_frame, font=('Times New Roman', 12))
                d.grid(row=i, column=j)
                d.insert(END, data[userID][i-1][j])
    
    for widget in test_frame.winfo_children():
        widget.grid_configure(padx=10)
#Display Function Movies
def display_recommendations_movie():
    for widget in test_frame.winfo_children():
        widget.destroy()
    movieID = movieId_entry.get()
    numberOfResults = int(numberOfResults_spinbox.get())

    idLabel = tkinter.Label(test_frame, text="Movie ID")
    idLabel.grid(row=0, column=0)
    movieLabel = tkinter.Label(test_frame, text="Movie Name")
    movieLabel.grid(row=0, column=1)
    ratingLabel = tkinter.Label(test_frame, text="Genres")
    ratingLabel.grid(row=0, column=2)
    cosineLabel = tkinter.Label(test_frame, text="Cosine Similarity Loss")
    cosineLabel.grid(row=0, column=3)
    
    for i in range(1, numberOfResults+2):
            for j in range(4):
                d = tkinter.Entry(test_frame, font=('Times New Roman', 12))
                d.grid(row=i, column=j)
                d.insert(END, dataMovie[movieID][i-1][j])
    
    for widget in test_frame.winfo_children():
        widget.grid_configure(padx=10)
#Display Function Genre
def display_recommendations_genre():
    for widget in test_frame.winfo_children():
        widget.destroy()
    movieGenreInput = movieGenre_entry.get()
    numberOfResults = int(numberOfResults_spinbox.get())

    movieLabel = tkinter.Label(test_frame, text="Movie ID")
    movieLabel.grid(row=0, column=0)
    movieNameLabel = tkinter.Label(test_frame, text="Movie Name")
    movieNameLabel.grid(row=0, column=1)
    genreLabel = tkinter.Label(test_frame, text="Rating")
    genreLabel.grid(row=0, column=2)
    
    for i in range(1, numberOfResults+1):
            for j in range(3):
                d = tkinter.Entry(test_frame, font=('Times New Roman', 12))
                d.grid(row=i, column=j)
                d.insert(END, dataGenre[movieGenreInput][i-1][j])
    
    for widget in test_frame.winfo_children():
        widget.grid_configure(padx=10)

#UI Structure 
#Window Set
window = tkinter.Tk()
window.title("Movie Recommendation System")

#Potential Image
'''bg = PhotoImage(file = "photo.png")
label1 = tkinter.Label(window, image = bg)
label1.place(x = 0, y = 0)'''

#Initial Frame Creation
frame = tkinter.Frame(window)
frame.pack()
frame.config(width=500)

#User-Input Frame and Child Widgets
user_input_frame = tkinter.LabelFrame(frame, text="User Input Area", font=('Times New Roman', 12))
user_input_frame.grid(row=0, column=0, padx=20, pady=10)

userId = tkinter.Label(user_input_frame, text="UserID", font=('Times New Roman', 12, 'bold'))
userId.grid(row=0, column=0)

movieId = tkinter.Label(user_input_frame, text="MovieID", font=('Times New Roman', 12, 'bold'))
movieId.grid(row=0, column=1)

movieGenre = tkinter.Label(user_input_frame, text="Movie Genre", font=('Times New Roman', 12, 'bold'))
movieGenre.grid(row=0, column=2)

numberOfResults = tkinter.Label(user_input_frame, text="Number of Results", font=('Times New Roman', 12, 'bold'))
numberOfResults.grid(row=0, column=3)

userId_entry = tkinter.Entry(user_input_frame)
movieId_entry = tkinter.Entry(user_input_frame)
movieGenre_entry = ttk.Combobox(user_input_frame, values=['Animation', 'Mystery', 'Romance', 'Film-Noir', 'Crime', 'Musical', 
          'IMAX', 'Horror', 'Adventure', 'Action', 'War', 'Drama', 'Sci-Fi', 'Western', 'Children', 'Documentary', 'Comedy', 'Thriller', 'Fantasy', 'genre'], font=('Times New Roman', 12))
numberOfResults_spinbox = tkinter.Spinbox(user_input_frame, from_=5, to=20)

userId_entry.grid(row=1, column=0)
movieId_entry.grid(row=1, column=1)
movieGenre_entry.grid(row=1, column=2)
numberOfResults_spinbox.grid(row=1, column=3)

button_user = tkinter.Button(user_input_frame, text="Search Recommendations by User", command= display_recommendations_user, font=('Times New Roman', 12))
button_user.grid(row=2, column=0)

button_movie = tkinter.Button(user_input_frame, text="Search Recommendations by Movie", command= display_recommendations_movie, font=('Times New Roman', 12))
button_movie.grid(row=2, column=1)

button_genre = tkinter.Button(user_input_frame, text="Search Recommendations by Genre", command= display_recommendations_genre, font=('Times New Roman', 12))
button_genre.grid(row=2, column=2)

for widget in user_input_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#Results Frame and Child Widgets
results_frame = tkinter.LabelFrame(frame, text="Results Area", font=('Times New Roman', 12))
results_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

recommendations_label = tkinter.Label(results_frame, text="Recommendations", font=('Times New Roman', 12, 'bold'))
recommendations_label.grid(row=0, column=0)
test_frame = tkinter.Frame(results_frame)
test_frame.grid(row=1, column=0)

for widget in results_frame.winfo_children():
    widget.grid_configure(padx=10)


window.mainloop()