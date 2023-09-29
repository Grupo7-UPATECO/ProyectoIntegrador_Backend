-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: discordio
-- ------------------------------------------------------
-- Server version	8.0.33

CREATE DATABASE discordio;
USE discordio;

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
-- Table structure for table `canales`
--

DROP TABLE IF EXISTS `canales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canales` (
  `id_canal` int NOT NULL AUTO_INCREMENT,
  `nombre_canal` varchar(150) NOT NULL,
  `id_servidor` int NOT NULL,
  PRIMARY KEY (`id_canal`),
  KEY `id_servidor` (`id_servidor`),
  CONSTRAINT `canales_ibfk_1` FOREIGN KEY (`id_servidor`) REFERENCES `servidor` (`id_servidor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canales`
--

LOCK TABLES `canales` WRITE;
/*!40000 ALTER TABLE `canales` DISABLE KEYS */;
INSERT INTO `canales` VALUES (1,'club de lectura',1),(2,'esscritores emergentes',1),(3,'recomendaciones',1),(4,'programacion con Python',2),(5,'programacion Java',2),(6,'tips entrevistas tecnicas',2);
/*!40000 ALTER TABLE `canales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chats`
--

DROP TABLE IF EXISTS `chats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chats` (
  `id_chat` int NOT NULL AUTO_INCREMENT,
  `chat` varchar(500) NOT NULL,
  `id_usuario` int NOT NULL,
  `id_canal` int NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_chat`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_canal` (`id_canal`),
  CONSTRAINT `chats_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `chats_ibfk_2` FOREIGN KEY (`id_canal`) REFERENCES `canales` (`id_canal`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chats`
--

LOCK TABLES `chats` WRITE;
/*!40000 ALTER TABLE `chats` DISABLE KEYS */;
INSERT INTO `chats` VALUES (1,'Est et kasd. Duo imperdiet et vel eos tempor dolor no facilisi lorem sea sed tempor. Rebum minim vel est sed nonumy blandit labore eros nostrud erat sanctus. Diam et dolore voluptua aliquyam ipsum dolor amet nostrud praesent aliquyam amet. Vero sed amet amet sea dolore eirmod eros sadipscing et wisi.',1,1,'2023-09-13 14:08:38'),(2,'Magna et magna. Ut assum sit accusam sit nonummy cum vel feugiat justo elitr facilisis dolore amet lorem veniam. Eirmod consequat ut facilisi exerci justo gubergren vero lorem stet sanctus.',1,1,'2023-09-13 14:08:38'),(3,'Aliquyam feugiat te et ea lorem ut eos at. Elitr nonumy tempor sed sit elit sed ut commodo ut est. Sanctus justo no dolore lorem magna. Iriure at illum diam dolore dolor sit stet stet et. Lorem takimata vel duo lorem sed diam accusam vulputate magna elitr duo gubergren aliquyam sea stet sadipscing elitr.',1,1,'2023-09-13 14:08:38'),(4,'Molestie commodo mazim. Erat labore quod et ex consequat ipsum gubergren. Volutpat diam ex sanctus justo dolore accumsan ad justo labore ipsum sit. Sed in wisi justo accumsan amet at amet est molestie vel. Illum elitr ea est sed eos option dolore erat accumsan labore ea facilisi gubergren.',3,2,'2023-09-17 20:02:11'),(5,'Molestie commodo mazim. Erat labore quod et ex consequat ipsum gubergren. Volutpat diam ex sanctus justo dolore accumsan ad justo labore ipsum sit. Sed in wisi justo accumsan amet at amet est molestie vel. Illum elitr ea est sed eos option dolore erat accumsan labore ea facilisi gubergren.',2,1,'2023-09-17 20:02:11'),(6,'Voluptua et eirmod augue ipsum kasd dolores. Nostrud eirmod voluptua esse duo et diam lorem gubergren et amet esse sed sanctus elitr et sea sit et. Ea est takimata ea amet possim dolor clita sadipscing rebum blandit dolor dolor esse. Autem nonummy sed sit amet ipsum gubergren dolore eirmod sed ipsum vel et diam dolor.',3,1,'2023-09-17 20:02:11'),(7,'Eirmod vulputate in lorem illum labore. Dolor aliquip sanctus tincidunt ipsum lorem ex autem ut dolores gubergren nobis. Et option at.',2,2,'2023-09-17 20:02:11'),(8,'Eirmod vulputate in lorem illum labore. Dolor aliquip sanctus tincidunt ipsum lorem ex autem ut dolores gubergren nobis. Et option at.',1,1,'2023-09-17 20:02:11'),(9,'Amet amet lorem delenit lorem dolor elitr sit dolore accumsan dolore dolore vero in eirmod. Et sed consetetur takimata duis. Amet clita duo sit sed. Consetetur voluptua amet magna justo et nostrud ea elitr hendrerit ex eum gubergren facilisi eos sea. Clita nonummy at duis eum accusam diam vel facer diam amet. Elitr no no at sed sit sanctus erat amet feugiat in sed eos accumsan dolor sed blandit vel eirmod.',3,2,'2023-09-17 20:02:11'),(10,'SELECT chats.id_chat, chats.chat, chats.id_usuario, usuarios.nombre_usuario, chats.id_canal, chats.fecha_creacion FROM discordio.chats ',2,3,'2023-09-17 20:04:03'),(11,'Amet amet lorem delenit lorem dolor elitr sit dolore accumsan dolore dolore vero in eirmod. Et sed consetetur takimata duis. Amet clita duo sit sed. Consetetur voluptua amet magna justo et nostrud ea elitr hendrerit ex eum gubergren facilisi eos sea. Clita nonummy at duis eum accusam diam vel facer diam amet. Elitr no no at sed sit sanctus erat amet feugiat in sed eos accumsan dolor sed blandit vel eirmod.',1,1,'2023-09-17 20:09:25'),(12,'Justo iusto at erat at. Dolor dolor lorem duo vero invidunt stet no eirmod lorem.',3,1,'2023-09-17 20:10:02');
/*!40000 ALTER TABLE `chats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servidor`
--

DROP TABLE IF EXISTS `servidor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servidor` (
  `id_servidor` int NOT NULL AUTO_INCREMENT,
  `nombre_servidor` varchar(150) NOT NULL,
  `id_usuario` int NOT NULL,
  PRIMARY KEY (`id_servidor`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `servidor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servidor`
--

LOCK TABLES `servidor` WRITE;
/*!40000 ALTER TABLE `servidor` DISABLE KEYS */;
INSERT INTO `servidor` VALUES (1,'Lectura',1),(2,'Programacion',1),(3,'Peliculas',1),(4,'Idiomas',3),(5,'Futbol',2),(6,'Hobbies',3);
/*!40000 ALTER TABLE `servidor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(20) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `contrasena` varchar(16) NOT NULL,
  `imagen_perfil` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'marta','marta','lopez','marta@correo.com','1234',NULL),(2,'pedrito','pedro','lopez','pedro@correo.com','1234',NULL),(3,'juani','juana','garcia','juana@correo.com','1234',NULL),(4,'jose23','jose','fernandezz','josefe@correo.com','1234',NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_servidor`
--

DROP TABLE IF EXISTS `usuarios_servidor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_servidor` (
  `id_usuarios_servidor` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_servidor` int NOT NULL,
  PRIMARY KEY (`id_usuarios_servidor`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_servidor` (`id_servidor`),
  CONSTRAINT `usuarios_servidor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `usuarios_servidor_ibfk_2` FOREIGN KEY (`id_servidor`) REFERENCES `servidor` (`id_servidor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_servidor`
--

LOCK TABLES `usuarios_servidor` WRITE;
/*!40000 ALTER TABLE `usuarios_servidor` DISABLE KEYS */;
INSERT INTO `usuarios_servidor` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,1),(5,2,2),(6,3,3),(7,3,4);
/*!40000 ALTER TABLE `usuarios_servidor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-17 18:56:46
