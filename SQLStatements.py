import sys
import sqlite3
from datetime import date





conn = sqlite3.connect("database.db")

#create database
def createDB():
    conn = sqlite3.connect("database.db")


# create a users table
def createUserTable():
    conn.execute('''CREATE TABLE IF NOT EXISTS users
            (userID             INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
             email              TEXT                                NOT NULL,
             password           VARCHAR(50)                         NOT NULL,
             phoneNumber        VARCHAR(50)                         NOT NULL,
             JoinDate           DATE                                NOT NULL,
             firstName          TEXT,
             surname            TEXT,
             dob                DATE,
             weight             REAL CHECK (weight>0),
             height             REAL CHECK (height>0),
             image              BLOB,
             bmi                REAL,
             startingWeight     REAL CHECK (startingWeight>0))
                                     ;''')




#create a food table
def createFoodTable():
    conn.execute('''CREATE TABLE IF NOT EXISTS food
            (foodID             INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
             foodType           TEXT                                NOT NULL,
             Calories           INTEGER(50) CHECK (Calories>0)      NOT NULL,
             Grams              INTEGER CHECK (Grams>0)             NOT NULL,
             mealType           TEXT                                NOT NULL,
             userID             TEXT                                NOT NULL,  
             AddedDate          DATE                                NOT NULL
             )
             
                                     ;''')

# create an exercise table
def createExerciseTable():
    conn.execute('''CREATE TABLE IF NOT EXISTS Exercise
             (ExerciseID             INTEGER PRIMARY KEY AUTOINCREMENT      NOT NULL,
              ExerciseType           TEXT                                   NOT NULL,
              CaloriesLost         INTEGER(50) CHECK (CaloriesLost>0)       NOT NULL,
              UserID                INTEGER                                 NOT NULL,
              AddedDate             DATE                                    NOT NULL
              )
                                      ;''')


# create a weightChange table
def createweightChangeTable():
    conn.execute('''CREATE TABLE IF NOT EXISTS weightChange
             (weightChangeID         INTEGER PRIMARY KEY AUTOINCREMENT      NOT NULL,
              weightChange          FLOAT                                 NOT NULL,
              UserID                INTEGER                                 NOT NULL
              )
                                      ;''')

#add information to exercise table
def addExercise(Exercise,Calories, userID):
    done = 'True'
    AddedDate = date.today()
    try:

        conn.execute("INSERT INTO Exercise (ExerciseType,CaloriesLost,UserID,AddedDate) VALUES(?,?,?,?)",
                     (Exercise, Calories, userID,AddedDate))
        conn.commit()

    except Exception as e:
        print(e)
        done = 'False'

    return done


#add food to food table
def addFood(FoodType, Calories, Grams, mealType, userID):
    done = 'True'
    AddedDate = date.today()
    try:

        conn.execute("INSERT INTO food (foodType,Calories,Grams,mealType,userID,AddedDate) VALUES(?,?,?,?,?,?)",
                     (FoodType, Calories, Grams, mealType, userID,AddedDate))
        conn.commit()

    except Exception as e:
        print(e)
        done = 'False'

    return done

def addWeightChange(userID,weight):


    userID = str(userID)
    userID = userID.replace("(","")
    userID = userID.replace(")", "")
    userID = userID.replace(",", "")

    try:
        conn.execute("INSERT INTO weightChange (weightChange,UserID) VALUES(?,?)",
                     (weight, userID))
        conn.commit()
        conn.commit()
    except Exception as e:
        print(e)



def updateWeight(userID, weight):
    complete = 'True'

    try:

        UserID = str(userID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))

        conn.execute("UPDATE users SET weight = '%s' WHERE userID = '%s'" % (UserID, weight))
        conn.commit()

    except Exception as e:
        print (e)
        complete = 'False'

    return complete

#add a user
def addUser(email, password, phoneNumber):
    done = 'True'

    JoinDate = date.today()
    try:
        name = 'user.png'
        with open(name, "rb") as f:
            data = f.read()
        data = data

        userExistsCheck = userExistsValidation(email)

        bmi = 20

        # if user doesnt exist, they will be added
        if (userExistsCheck == False):
            conn.execute("INSERT INTO users (email,password,JoinDate,phoneNumber,bmi,image) VALUES(?,?,?,?,?,?)",
                         (email, password, JoinDate, phoneNumber,bmi,data))
            conn.commit()
        else:
            done = 'checkFailed'

    except Exception:
        # could not be added
        done = 'False'

    return done

#add users additional information
def addUserInfo(e, pw, pn, fn, sn, dateOfBirth, w, h, sw):
    JoinDate = date.today()

    done = 'True'

    userExistsCheck = userExistsValidation(e)

    try:
        if (userExistsCheck == False):
            conn.execute(
                "INSERT INTO users (email,password,phoneNumber,JoinDate,firstName,surname,dob,weight,height,startingWeight) VALUES(?,?,?,?,?,?,?,?,?,?)",
                (e, pw, pn, JoinDate, fn, sn, dateOfBirth, w, h, sw))
            conn.commit()
        else:
            done = 'checkFailed'

    except Exception as e:
        print(e)
        done = 'false'

    return done




#check if email already exists
def userExistsValidation(emailToCheck):
    # boolean for if user exists
    boolean = False;

    # select all clients email
    userExistsQuery = conn.execute("SELECT email FROM users")
    records = userExistsQuery.fetchall()

    # loop for every email
    for row in records:

        # if the email already exists
        if ((str(row[0])) == emailToCheck):
            # set check to true
            boolean = True;
            # if found loop will stop
            break
    return boolean

#ccheck if email already exists
def usersStartingweightValidation(idToCheck):
    # boolean for if user exists
    boolean = False;

    # select all clients ids
    userExistsQuery = conn.execute("SELECT userID FROM weightChange")
    records = userExistsQuery.fetchall()

    idToCheck = str(idToCheck)
    idToCheck = (idToCheck.replace("(", ""))
    idToCheck = (idToCheck.replace(")", ""))
    idToCheck = (idToCheck.replace(",", ""))

    # loop for every email
    for row in records:

        # if the email already exists
        if ((str(row[0])) == str(idToCheck)):
            # set check to true
            boolean = True;

            # if found loop will stop
            break
    return boolean

#ccheck if email already exists
def usersStartingweightValidation(idToCheck):
    # boolean for if user exists
    boolean = False;

    # select all clients ids
    userExistsQuery = conn.execute("SELECT userID FROM weightChange")
    records = userExistsQuery.fetchall()

    idToCheck = str(idToCheck)
    idToCheck = (idToCheck.replace("(", ""))
    idToCheck = (idToCheck.replace(")", ""))
    idToCheck = (idToCheck.replace(",", ""))

    # loop for every email
    for row in records:

        # if the email already exists
        if ((str(row[0])) == str(idToCheck)):
            # set check to true
            boolean = True;

            # if found loop will stop
            break
    return boolean


#check if passwords match
def checkPassword(userID):
    infoQuery = conn.execute("SELECT password FROM users WHERE userID= '%s'" % (userID))
    records = infoQuery.fetchall()
    password = records[0]
    return password

#get users ID from their email
def getUserID(email):
    infoQuery = conn.execute("SELECT userID FROM users WHERE email= '%s'" % (email))
    records = infoQuery.fetchall()

    if str(records) == "[]":
        return "NoUser"
    else:
        return records[0]

def getBmi(userID):
    try:
        UserID = str(userID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))


        result = conn.execute("SELECT bmi FROM users WHERE userID ='%s'"%  (UserID))
        records = result.fetchall()
        bmi = records[0]
        bmi = str(bmi)

        bmi = (bmi.replace("(",""))
        bmi = (bmi.replace(")", ""))
        bmi = (bmi.replace(",", ""))
        bmi = float(bmi)
        bmi = int(bmi)
        return bmi

    except Exception as e:
        print (e)

def getBreakfastInfo(userID,Date):
    try:
        UserID = str(userID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))


        result = conn.execute("SELECT foodType,Calories,Grams FROM food WHERE AddedDate ='%s' AND userID ='%s' AND mealType = 'Breakfast'"%  (Date,UserID))

        return result

    except Exception as e:
        print (e)

def getallWeightChanges(userID):
    try:
        UserID = str(userID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))


        result = conn.execute("SELECT weightChange FROM weightChange WHERE userID ='%s' "%  (UserID))
        records = result.fetchall()
        print(records)

        return records

    except Exception as e:
        print (e)

def getlunchInfo(userID,Date):
    try:
        UserID = str(userID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))


        result = conn.execute("SELECT foodType,Calories,Grams FROM food WHERE AddedDate ='%s' AND userID ='%s' AND mealType = 'Lunch'"%  (Date,UserID))

        return result

    except Exception as e:
        print (e)


def getDinnerInfo(userID,Date):
    try:
        UserID = str(userID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))


        result = conn.execute("SELECT foodType,Calories,Grams FROM food WHERE AddedDate ='%s' AND userID ='%s' AND mealType = 'Dinner'"%  (Date,UserID))

        return result

    except Exception as e:
        print (e)


def getSnackInfo(userID,Date):
    try:
        UserID = str(userID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))


        result = conn.execute("SELECT foodType,Calories,Grams FROM food WHERE AddedDate ='%s' AND userID ='%s' AND mealType = 'Snack'"%  (Date,UserID))

        return result

    except Exception as e:
        print (e)

def getExerciseInfo(userID,Date):
    try:
        UserID = str(userID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))


        result = conn.execute("SELECT ExerciseType,CaloriesLost FROM Exercise WHERE AddedDate ='%s' AND userID ='%s'"%  (Date,UserID))

        return result

    except Exception as e:
        print (e)

def getTotalBreakfastCalories(userID,Date):
    UserID = str(userID)
    UserID = (UserID.replace("(", ""))
    UserID = (UserID.replace(")", ""))
    UserID = (UserID.replace(",", ""))

    totalCaloriesQuery = conn.execute(
        "SELECT sum(Calories) FROM food WHERE AddedDate ='%s' AND userID ='%s' AND mealType = 'Breakfast'" % (Date, UserID))
    result = totalCaloriesQuery.fetchall()
    return result


def getTotalLunchCalories(userID,Date):
    UserID = str(userID)
    UserID = (UserID.replace("(", ""))
    UserID = (UserID.replace(")", ""))
    UserID = (UserID.replace(",", ""))

    totalCaloriesQuery = conn.execute(
        "SELECT sum(Calories) FROM food WHERE AddedDate ='%s' AND userID ='%s' AND mealType = 'Lunch'" % (Date, UserID))
    result = totalCaloriesQuery.fetchall()

    return result


def getTotalDinnerCalories(userID,Date):
    UserID = str(userID)
    UserID = (UserID.replace("(", ""))
    UserID = (UserID.replace(")", ""))
    UserID = (UserID.replace(",", ""))

    totalCaloriesQuery = conn.execute(
        "SELECT sum(Calories) FROM food WHERE AddedDate ='%s' AND userID ='%s' AND mealType = 'Dinner'" % (Date, UserID))
    result = totalCaloriesQuery.fetchall()
    return result


def getTotalSnacksCalories(userID,Date):
    UserID = str(userID)
    UserID = (UserID.replace("(", ""))
    UserID = (UserID.replace(")", ""))
    UserID = (UserID.replace(",", ""))

    totalCaloriesQuery = conn.execute(
        "SELECT sum(Calories) FROM food WHERE AddedDate ='%s' AND userID ='%s' AND mealType = 'Snack'" % (Date, UserID))
    result = totalCaloriesQuery.fetchall()
    return result


def getTotalExerciseCalories(userID):
     totalCaloriesQuery = conn.execute("select sum(CaloriesLost) from Exercise WHERE userID ='%s'" % (userID))
     result = totalCaloriesQuery.fetchall()
     return result

def getJoinDate(userID):
    joinDateQuery = conn.execute("select JoinDate from users WHERE userID= '%s'" % (userID))
    result = joinDateQuery.fetchall()
    return result

def getStartingWeight(userID):
    UserID = str(userID)
    UserID = (UserID.replace("(", ""))
    UserID = (UserID.replace(")", ""))
    UserID = (UserID.replace(",", ""))

    startingWeightQuery = conn.execute("select startingWeight from users WHERE userID= '%s'" % (UserID))
    startingweight = startingWeightQuery.fetchall()

    startingweight = str(startingweight)
    startingweight = (startingweight.replace("[", ""))
    startingweight = (startingweight.replace("]", ""))
    startingweight = (startingweight.replace("(", ""))
    startingweight = (startingweight.replace(")", ""))
    startingweight = (startingweight.replace(",", ""))
    return startingweight

def getCurrentWeight(userID):
    UserID = str(userID)
    UserID = (UserID.replace("(", ""))
    UserID = (UserID.replace(")", ""))
    UserID = (UserID.replace(",", ""))

    currentweightQuery = conn.execute("select weight from users WHERE userID= '%s'" % (UserID))
    currentweight = currentweightQuery.fetchall()

    currentweight = str(currentweight)
    currentweight = (currentweight.replace("[", ""))
    currentweight = (currentweight.replace("]", ""))
    currentweight = (currentweight.replace("(", ""))
    currentweight = (currentweight.replace(")", ""))
    currentweight = (currentweight.replace(",", ""))
    return currentweight


def getTotalCalories(userID):
    Date = date.today()
    UserID = str(userID)
    UserID = (UserID.replace("(", ""))
    UserID = (UserID.replace(")", ""))
    UserID = (UserID.replace(",", ""))

    TotalCaloriesQuery = conn.execute("SELECT sum(Calories) FROM food WHERE AddedDate ='%s' AND userID ='%s'"%  (Date,UserID))
    totalCalories = TotalCaloriesQuery.fetchall()

    totalCalories = str(totalCalories)
    totalCalories = (totalCalories.replace("[",""))
    totalCalories = (totalCalories.replace("]", ""))
    totalCalories = (totalCalories.replace("(", ""))
    totalCalories = (totalCalories.replace(")", ""))
    totalCalories = (totalCalories.replace(",", ""))
    return totalCalories


def getUserName(userID):
    FirstNameQuery = conn.execute("SELECT firstName FROM users WHERE userID ='%s'"%  (userID))
    LastNameQuery = conn.execute("SELECT surname FROM users WHERE userID ='%s'" % (userID))
    FirstName = FirstNameQuery.fetchall()
    LastName = LastNameQuery.fetchall()

    FirstName = str(FirstName)
    FirstName = (FirstName.replace("[",""))
    FirstName = (FirstName.replace("]", ""))
    FirstName = (FirstName.replace("(", ""))
    FirstName = (FirstName.replace(")", ""))
    FirstName = (FirstName.replace(",", ""))
    FirstName = (FirstName.replace("'", ""))

    LastName = str(LastName)
    LastName = (LastName.replace("[",""))
    LastName = (LastName.replace("]", ""))
    LastName = (LastName.replace("(", ""))
    LastName = (LastName.replace(")", ""))
    LastName = (LastName.replace(",", ""))
    LastName = (LastName.replace("'", ""))

    Fullname = str(FirstName + " " + LastName)
    return Fullname

def getWeight(userID):
    weightQuery = conn.execute("SELECT weight FROM users WHERE userID ='%s'"%  (userID))
    weight = weightQuery.fetchall()


    weight = str(weight)
    weight = (weight.replace("[",""))
    weight = (weight.replace("]", ""))
    weight = (weight.replace("(", ""))
    weight = (weight.replace(")", ""))
    weight = (weight.replace(",", ""))
    weight = (weight.replace("'", ""))
    return weight

def getHeight(userID):
    heightQuery = conn.execute("SELECT height FROM users WHERE userID ='%s'"%  (userID))
    height = heightQuery.fetchall()


    height = str(height)
    height = (height.replace("[",""))
    height = (height.replace("]", ""))
    height = (height.replace("(", ""))
    height = (height.replace(")", ""))
    height = (height.replace(",", ""))
    height = (height.replace("'", ""))

    return height

def getCaloriesLeft(userID):
    Date = date.today()
    UserID = str(userID)
    UserID = (UserID.replace("(", ""))
    UserID = (UserID.replace(")", ""))
    UserID = (UserID.replace(",", ""))

    TotalCaloriesQuery = conn.execute("SELECT sum(Calories) FROM food WHERE AddedDate ='%s' AND userID ='%s'"%  (Date,UserID))
    totalCalories = TotalCaloriesQuery.fetchall()

    totalCalories = str(totalCalories)
    totalCalories = (totalCalories.replace("[",""))
    totalCalories = (totalCalories.replace("]", ""))
    totalCalories = (totalCalories.replace("(", ""))
    totalCalories = (totalCalories.replace(")", ""))
    totalCalories = (totalCalories.replace(",", ""))

    TotalExerciseQuery = conn.execute("SELECT sum(CaloriesLost) FROM Exercise WHERE AddedDate ='%s' AND userID ='%s'"%  (Date,UserID))
    TotalExercise = TotalExerciseQuery.fetchall()

    TotalExercise = str(TotalExercise)
    TotalExercise = (TotalExercise.replace("[",""))
    TotalExercise = (TotalExercise.replace("]", ""))
    TotalExercise = (TotalExercise.replace("(", ""))
    TotalExercise = (TotalExercise.replace(")", ""))
    TotalExercise = (TotalExercise.replace(",", ""))

    TotalExercise = int(TotalExercise)
    totalCalories = int(totalCalories)
    Total = str(1800 + TotalExercise - totalCalories )
    return Total

def AddImage(data,UserID):
    try:
        UserID = str(UserID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))

        conn.execute("UPDATE users SET image = (?) WHERE userID = (?)", (data, UserID))
        conn.commit()
    except Exception as e:
        print(e)



def changeBmi(data,UserID):
    try:
        UserID = str(UserID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))

        conn.execute("UPDATE users SET bmi = (?) WHERE userID = (?)", (data, UserID))
        conn.commit()
    except Exception as e:
        print(e)

def showImage(UserID):
    try:
        UserID = str(UserID)
        UserID = (UserID.replace("(", ""))
        UserID = (UserID.replace(")", ""))
        UserID = (UserID.replace(",", ""))

        query = conn.execute("SELECT * FROM users WHERE userID = (?)",(UserID))
        result = query.fetchone()
        image = result[10]

        return image




    except Exception as e:
        print("hi")
