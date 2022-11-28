from markett import app



#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)






app.debug = True
app.run(debug=True, use_debugger=False, use_reloader=False)
