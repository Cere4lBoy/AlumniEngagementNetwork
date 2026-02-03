CREATE DATABASE aens_db;
USE aens_db;

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Role ENUM('student', 'alumni', 'admin', 'cso') NOT NULL,
    PhoneNumber VARCHAR(20)
);

CREATE TABLE Student (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT UNIQUE,
    Major VARCHAR(100),
    EnrollmentYear YEAR,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE Alumni (
    AlumniID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT UNIQUE,
    GraduationYear YEAR,
    CurrentJob VARCHAR(100),
    Industry VARCHAR(100),
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE Career_Officer (
    OfficerID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT UNIQUE,
    Department VARCHAR(100),
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE Admin (
    AdminID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT UNIQUE,
    AdminLevel VARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE Notification (
    NotificationID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    Message TEXT,
    Type VARCHAR(50),
    IsRead BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    Category VARCHAR(50),
    Comments TEXT,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE Event (
    EventID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    Description TEXT,
    EventDate DATE,
    Location VARCHAR(100),
    CreatedBy_AdminID INT,
    FOREIGN KEY (CreatedBy_AdminID) REFERENCES Admin(AdminID)
);

CREATE TABLE Event_Registration (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    EventID INT,
    RegistrationDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (EventID) REFERENCES Event(EventID)
);

CREATE TABLE Job_Post (
    JobID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    Description TEXT,
    Requirements TEXT,
    Status VARCHAR(50),
    PostedBy_AlumniID INT,
    ApprovedBy_OfficerID INT,
    FOREIGN KEY (PostedBy_AlumniID) REFERENCES Alumni(AlumniID),
    FOREIGN KEY (ApprovedBy_OfficerID) REFERENCES Career_Officer(OfficerID)
);

CREATE TABLE Job_Application (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY,
    JobID INT,
    StudentID INT,
    AppliedDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (JobID) REFERENCES Job_Post(JobID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

CREATE TABLE Mentorship_Request (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,
    Mentee_StudentID INT,
    Mentor_AlumniID INT,
    Goals TEXT,
    Reason TEXT,
    Status VARCHAR(50),
    FOREIGN KEY (Mentee_StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (Mentor_AlumniID) REFERENCES Alumni(AlumniID)
);

CREATE TABLE Testimonial (
    TestimonialID INT AUTO_INCREMENT PRIMARY KEY,
    AlumniID INT,
    Content TEXT,
    DateSubmitted DATE,
    IsApproved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (AlumniID) REFERENCES Alumni(AlumniID)
);
