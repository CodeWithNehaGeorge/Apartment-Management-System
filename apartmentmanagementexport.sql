-- MySQL dump 10.13  Distrib 5.5.10, for Win64 (x86)
--
-- Host: localhost    Database: apartmentmanagement
-- ------------------------------------------------------
-- Server version	5.5.10

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `flat`
--

DROP TABLE IF EXISTS `flat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flat` (
  `FLAT_NUMBER` varchar(20) NOT NULL,
  `FLOOR` int(11) DEFAULT NULL,
  `AREA` int(11) DEFAULT NULL,
  `TYPE` varchar(20) DEFAULT NULL,
  `OWNER_STATUS` varchar(20) DEFAULT NULL,
  `MAINTENANCE_FEE` int(11) DEFAULT NULL,
  PRIMARY KEY (`FLAT_NUMBER`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flat`
--

LOCK TABLES `flat` WRITE;
/*!40000 ALTER TABLE `flat` DISABLE KEYS */;
INSERT INTO `flat` VALUES ('1A',1,1500,'A','Tenant',1500),('1B',1,1875,'B','Tenant',1700),('1C',1,2150,'C','Owner',1850),('1D',1,2500,'D','Owner',2100),('2A',2,1500,'A','Owner',1500),('2B',2,1875,'B','Tenant',1700),('2C',2,2150,'C','Owner',1850),('2D',2,2500,'D','Tenant',2100),('3A',3,1500,'A','Owner',1500),('3B',3,1875,'B','Owner',1700);
/*!40000 ALTER TABLE `flat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintenance_fee`
--

DROP TABLE IF EXISTS `maintenance_fee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_fee` (
  `RECEIPT_ID` int(11) NOT NULL,
  `FLAT_NUMBER` varchar(5) NOT NULL,
  `MONTH` varchar(10) DEFAULT NULL,
  `AMOUNT_PAID` int(11) DEFAULT NULL,
  `AMOUNT_DUE` int(11) DEFAULT NULL,
  PRIMARY KEY (`RECEIPT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintenance_fee`
--

LOCK TABLES `maintenance_fee` WRITE;
/*!40000 ALTER TABLE `maintenance_fee` DISABLE KEYS */;
INSERT INTO `maintenance_fee` VALUES (1001,'1A','February',1400,1000),(1002,'1B','February',1700,0),(1003,'1C','February',1800,50),(1004,'1D','February',1000,1100),(1005,'2A','February',0,1500),(1006,'2B','February',200,1300),(1007,'2C','February',1200,650),(1008,'2D','February',1300,800),(1009,'3A','February',1000,500),(1010,'3B','February',0,1700);
/*!40000 ALTER TABLE `maintenance_fee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `residentmanagement`
--

DROP TABLE IF EXISTS `residentmanagement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `residentmanagement` (
  `RESIDENT_ID` int(11) NOT NULL,
  `RESIDENT_NAME` varchar(20) DEFAULT NULL,
  `FLAT_NUMBER` varchar(6) DEFAULT NULL,
  `CONTACT_NUMBER` varchar(20) DEFAULT NULL,
  `EMAIL_ID` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`RESIDENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residentmanagement`
--

LOCK TABLES `residentmanagement` WRITE;
/*!40000 ALTER TABLE `residentmanagement` DISABLE KEYS */;
INSERT INTO `residentmanagement` VALUES (1001,'Helen','1A','9856473649','helen2000@gmail.com'),(1002,'John','1B','7652897465','johnpeter123@gmail.com'),(1003,'Hiba','1C','8764578023','hibanoorin@gmail.com'),(1004,'Andrew','1D','9863647543','andrewmartin@gmail.com'),(1005,'James','2A','8975431234','jamesrodriguez@gmail.com'),(1006,'Taylor','2B','6786679979','taylorharris@gmail.com'),(1007,'Jessica','2C','9876450923','jessica23009@gmail.com'),(1008,'Michele','2D','9807865460','michelewilliam@gmail.com'),(1009,'Steve','3A','8765434120','steveparker82@gmail.com'),(1010,'Jennifer','3B','7654892310','jenniferholland@gmail.com');
/*!40000 ALTER TABLE `residentmanagement` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-13 21:15:26
