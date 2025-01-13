-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `Patient_ID` char(4) DEFAULT NULL,
  `appointment_date` date NOT NULL,
  `appointment_time` time NOT NULL,
  `Patient_Name` varchar(25) DEFAULT NULL,
  `doctor` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `Patient_ID` varchar(15) NOT NULL,
  `Patient_Name` varchar(30) NOT NULL,
  `appointment_date` char(15) DEFAULT NULL,
  `appointment_time` char(15) DEFAULT NULL,
  `Doctor_Name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Patient_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES ('P101','Rounak D.','12-02-2023','10:30','Kriti B.'),('P102','Priyesh B.','13-02-2023','10:45','Bikash B.'),('P103','Abhishek R.','13-02-2023','11:00','B.P.'),('P104','Vaibhav R.','14-02-2023','10:30','Vikram R.'),('P105','Kapish B.','14-02-2023','11:00','Baichung'),('P106','Yash B.','15-02-2023','10:00','Sunita S.');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bills`
--

DROP TABLE IF EXISTS `bills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bills` (
  `pid` varchar(25) DEFAULT NULL,
  `item` varchar(40) DEFAULT NULL,
  `amount` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills`
--

LOCK TABLES `bills` WRITE;
/*!40000 ALTER TABLE `bills` DISABLE KEYS */;
INSERT INTO `bills` VALUES ('7896','uygh',890),('7896','a1',1111),('7896','ftuyg',7890),('7896','uygk',111111),('7896','tyf8i7',564),('7896','123',134),('fgbdnfh','8675',987656),('fgbdnfh','yvu',8976),('76','76',76),('P103','Bandage',100),('P103','Bedding',1000),('P103','Glucose',400),('P103','Medicines',2000),('P101','Bedding',500),('P101','Glucose',500);
/*!40000 ALTER TABLE `bills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `User_ID` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  PRIMARY KEY (`User_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('Madhur','12345'),('Rishav','12345'),('Sujay','12345');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pat`
--

DROP TABLE IF EXISTS `pat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pat` (
  `Patient_ID` varchar(25) NOT NULL,
  `Patient_Name` varchar(25) NOT NULL,
  `dob` char(12) DEFAULT NULL,
  `no` bigint DEFAULT NULL,
  `age` int DEFAULT NULL,
  `doctor` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Patient_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pat`
--

LOCK TABLES `pat` WRITE;
/*!40000 ALTER TABLE `pat` DISABLE KEYS */;
INSERT INTO `pat` VALUES ('P101','Rounak D.','12-08-2002',919908710,20,'Kriti B.'),('P102','Priyesh B.','12-12-2001',8976589756,21,'Bikash B.'),('P103','Abhishek R.','03-11-2000',7835709756,22,'B.P.'),('P104','Vaibhav R.','07-11-2005',856745765,17,'Vikram R.'),('P105','Kapish B.','08-09-2000',9564598345,22,'Baichung'),('P106','Yash B.','26-01-2006',5698734987,17,'Sunita S.');
/*!40000 ALTER TABLE `pat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `Patient_ID` char(4) NOT NULL,
  `Patient_Name` varchar(25) NOT NULL,
  `dob` date DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  `age` int DEFAULT NULL,
  `doctor` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Patient_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `D_id` char(10) NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `dob` char(12) DEFAULT NULL,
  `category` varchar(25) DEFAULT NULL,
  `speciality` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`D_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES ('P108','Krishna S.',20,'03-11-2002','Doctor','Surgeon'),('S101','Abhijeet B.',34,'12-12-1988','Doctor','Orthopedics'),('S102','Yashwant S.',42,'08-10-1980','Doctor','Neurology'),('S103','Prateek N.',40,'08-10-1982','Doctor','Pediatrician'),('S104','Geeta B.',34,'10-12-1988','Doctor','Gynecology'),('S105','Anushka S.',24,'10-12-1998','Nurse','Dressing'),('S106','Kareena K.',32,'07-07-1990','Doctor','Surgery'),('S107','Chiya S.',20,'26-12-2002','Nurse','Assisting');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staffs`
--

DROP TABLE IF EXISTS `staffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staffs` (
  `id` char(4) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `age` int DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `category` varchar(25) DEFAULT NULL,
  `speciality` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staffs`
--

LOCK TABLES `staffs` WRITE;
/*!40000 ALTER TABLE `staffs` DISABLE KEYS */;
/*!40000 ALTER TABLE `staffs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-13 23:23:35
