-- MySQL dump 10.13  Distrib 5.7.29, for osx10.15 (x86_64)
--
-- Host: localhost    Database: issue_tracking
-- ------------------------------------------------------
-- Server version	5.7.29

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
-- Table structure for table `complaints`
--

DROP TABLE IF EXISTS `complaints`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `complaints` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cdata` varchar(500) NOT NULL,
  `tags` varchar(500) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `complaints`
--

LOCK TABLES `complaints` WRITE;
/*!40000 ALTER TABLE `complaints` DISABLE KEYS */;
/*!40000 ALTER TABLE `complaints` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resolvers`
--

DROP TABLE IF EXISTS `resolvers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resolvers` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `rname` varchar(40),
  `remail` varchar(40) NOT NULL,
  `rposition` varchar(50) NOT NULL,
  `rpin` varchar(50),
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resolvers`
--

LOCK TABLES `resolvers` WRITE;
/*!40000 ALTER TABLE `resolvers` DISABLE KEYS */;
/*!40000 ALTER TABLE `resolvers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resolves`
--

DROP TABLE IF EXISTS `resolves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resolves` (
  `rid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `is_valid` bit(1) DEFAULT NULL,
  `is_resolved` bit(1) DEFAULT NULL,
  KEY `rid` (`rid`),
  KEY `cid` (`cid`),
  CONSTRAINT `resolves_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `resolvers` (`rid`),
  CONSTRAINT `resolves_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `complaints` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resolves`
--

LOCK TABLES `resolves` WRITE;
/*!40000 ALTER TABLE `resolves` DISABLE KEYS */;
/*!40000 ALTER TABLE `resolves` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sfiles`
--

DROP TABLE IF EXISTS `sfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sfiles` (
  `sid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `ftime` date NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`cid`,`sid`),
  KEY `sid` (`sid`),
  CONSTRAINT `sfiles_ibfk_1` FOREIGN KEY (`sid`) REFERENCES `students` (`sid`),
  CONSTRAINT `sfiles_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `complaints` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sfiles`
--

LOCK TABLES `sfiles` WRITE;
/*!40000 ALTER TABLE `sfiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `sfiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(40),
  `Semail` varchar(40) NOT NULL,
  `spin` varchar(100),
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teachers` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(40),
  `temail` varchar(40) NOT NULL,
  `tpin` varchar(100),
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tfiles`
--

DROP TABLE IF EXISTS `tfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tfiles` (
  `tid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `ftime` date NOT NULL,
  PRIMARY KEY (`cid`,`tid`),
  KEY `tid` (`tid`),
  CONSTRAINT `tfiles_ibfk_1` FOREIGN KEY (`tid`) REFERENCES `teachers` (`tid`),
  CONSTRAINT `tfiles_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `complaints` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tfiles`
--

LOCK TABLES `tfiles` WRITE;
/*!40000 ALTER TABLE `tfiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `tfiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-30 22:36:02
