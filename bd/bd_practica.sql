-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: bd_practica
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `nombre_categoria` varchar(45) NOT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'almacen'),(2,'bebidas'),(3,'carniceria'),(4,'congelados'),(5,'fiambreria'),(6,'lacteos'),(7,'limpieza'),(8,'panaderia'),(9,'perfumeria'),(10,'snacks'),(11,'verduleria');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nom_cliente` varchar(45) NOT NULL,
  `ap_cliente` varchar(45) NOT NULL,
  `calle_cliente` varchar(45) NOT NULL,
  `ncalle_cliente` int NOT NULL,
  `dni_cliente` bigint NOT NULL,
  `correo_cliente` varchar(50) NOT NULL,
  `telefono_cliente` bigint NOT NULL,
  `privilegios` int DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `dni_cliente_UNIQUE` (`dni_cliente`),
  UNIQUE KEY `telefono_cliente_UNIQUE` (`telefono_cliente`),
  UNIQUE KEY `correo_cliente_UNIQUE` (`correo_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Julian','Perez','Saavedra ',1070,42505240,'juliangaldamez0@gmail.com',2604600688,1),(2,'david ','veisaga','castelli ',504,18123453,'davidveisaga1@gmail.com',2604834935,NULL),(3,'ramon','perez','paunero ',123,44125005,'ramonperez2@gmail.com',2604009855,NULL),(4,'roman ','riquelme','boca ',12,20543521,'romanriquelme3@gmail.com',2604928348,NULL),(5,'martin ','palermo','granaderos ',505,23524069,'martinpalermo4@gmail.com',2604104123,NULL),(6,'nestor ','benegas','independencia ',910,16505123,'nestorbenegas5@gmail.com',2604123443,NULL),(7,'zulema ','caballero','saavedra ',1070,16836454,'zulemacaballero6@gmail.com',2604667533,NULL),(8,'Julio Cesar','Galdamez','Anglat',881,18357181,'juliocegaldamez@gmail.com',2604570666,NULL),(9,'sebastian ','gonzalez','matienzo ',530,44536826,'sebastiangonzalez8@gmail.com',2604810299,NULL),(10,'maria ','lopez','salta ',1220,38005129,'marialopez9@gmail.com',2605234352,NULL),(11,'Esteban','Mcalister','El Molino',124142412,123,'juliangaldamez0124124@gmail.com',1324124,NULL),(12,'julian','veisaga','Fucsias',124235,10,'juliangaldamez124121110@gmail.com',421542,NULL),(14,'Stevie','Counsell','Kings',31,553810480,'scounsell0@google.it',3053854030,NULL),(15,'Glori','Hazelden','Westridge',26,5194010257,'ghazelden1@wikipedia.org',3087001003,NULL),(16,'Angelina','Garnul','Kedzie',4,153958642,'agarnul2@ed.gov',9852860341,NULL),(17,'Domini','Palleske','Porter',61689,1774518406,'dpalleske3@sogou.com',5324811630,NULL),(18,'Zeke','Farr','Sachtjen',1,7476365860,'zfarr4@webeden.co.uk',5007252356,NULL),(19,'Nicoline','Rowledge','Green Ridge',3979,7803329438,'nrowledge5@angelfire.com',7111457534,NULL),(20,'Krystyna','Mattusevich','Eagle Crest',311,6377549873,'kmattusevich6@technorati.com',3891058161,NULL),(21,'Dionysus','Stockoe','Trailsway',1935,4759926127,'dstockoe7@ibm.com',4929300013,NULL),(22,'Erhard','Canet','Sugar',525,4188608579,'ecanet8@indiegogo.com',8749718751,NULL),(23,'Arny','Cornthwaite','Almo',2142,5840831689,'acornthwaite9@cdbaby.com',8386747151,NULL),(24,'Grantham','Joderli','Erie',9,4316718177,'gjoderlia@clickbank.net',3724096366,NULL),(25,'Marinna','Titford','Judy',9653,5882456061,'mtitfordb@digg.com',3033584272,NULL),(26,'Koren','Lithgow','Arapahoe',50,2307249672,'klithgowc@un.org',7803639304,NULL),(27,'Cary','Carp','Del Mar',256,2291841254,'ccarpd@hatena.ne.jp',3288170134,NULL),(28,'Currey','Delaney','Fuller',46,1161664807,'cdelaneye@springer.com',7677793803,NULL),(29,'Christie','Ringsell','Hudson',773,1515471039,'cringsellf@yelp.com',6584145796,NULL),(30,'Ranna','Marchant','Walton',3,4585065512,'rmarchantg@opera.com',4466508984,NULL),(31,'Saul','Swadden','Corben',9245,6570293540,'sswaddenh@kickstarter.com',4721262296,NULL),(32,'Reyna','Fishburn','Acker',3,7767748863,'rfishburni@umn.edu',1166446971,NULL),(33,'Bea','Gowanlock','Randy',2986,1153555999,'bgowanlockj@constantcontact.com',1472314302,NULL),(34,'Sasha','Bedbrough','Kings',45163,3319243578,'sbedbroughk@tinyurl.com',9124999627,NULL),(35,'Louella','Yukhnev','Comanche',3,9073816262,'lyukhnevl@fastcompany.com',7691107831,NULL),(36,'Jill','Nazer','Maryland',5336,4809110818,'jnazerm@ihg.com',4403149259,NULL),(37,'Flossy','Nolot','Birchwood',35,3708877195,'fnolotn@pagesperso-orange.fr',9869095240,NULL),(38,'Selma','Scotchmur','Summer Ridge',550,9988827806,'sscotchmuro@behance.net',4221121121,NULL),(39,'Ulrikaumeko','Terzza','Chive',6,457437448,'uterzzap@tinypic.com',3716554628,NULL),(40,'Atlanta','Firks','Eagle Crest',83930,5620408485,'afirksq@devhub.com',6071427380,NULL),(41,'Danice','Gorman','Prairie Rose',5,979979048,'dgormanr@globo.com',2903580665,NULL),(42,'Willard','Largen','Stuart',8,6261502692,'wlargens@cbsnews.com',5097953824,NULL),(43,'Egbert','Cavolini','Merry',8,3707789675,'ecavolinit@soundcloud.com',9455302947,NULL),(44,'Hank','Oliveto','Ramsey',80486,8814808686,'holivetou@nhs.uk',2021254335,NULL),(45,'Bridget','Pavkovic','Vidon',51,8187766646,'bpavkovicv@tripadvisor.com',4053256207,NULL),(46,'Lem','Saddler','Briar Crest',722,7172931335,'lsaddlerw@google.com.hk',5734148311,NULL),(47,'Amelia','Layus','Reindahl',85547,4983003886,'alayusx@foxnews.com',3246224775,NULL),(48,'Cherin','McCrisken','Holy Cross',8389,9709212974,'cmccriskeny@google.de',6674162749,NULL),(49,'Daron','Dunbleton','Arkansas',2,5038300774,'ddunbletonz@unc.edu',1003679289,NULL),(50,'Arte','Ellor','Vernon',805,4614629172,'aellor10@tamu.edu',5679908958,NULL),(51,'Gabbie','Gorry','Hanson',469,4025478676,'ggorry11@bloglines.com',7112077298,NULL),(52,'Gabriele','Elsay','Lighthouse Bay',51,1616977094,'gelsay12@amazon.co.jp',7752927983,NULL),(53,'Felix','Edwicker','6th',2,9852926748,'fedwicker13@xing.com',1246441892,NULL),(54,'Shana','Edmund','Texas',4,1372228403,'sedmund14@barnesandnoble.com',2324351495,NULL),(55,'Augustus','Kindleside','Declaration',9802,274999250,'akindleside15@cbslocal.com',8998609756,NULL),(56,'Arvie','Benois','Logan',57,278093051,'abenois16@nps.gov',7062133845,NULL),(57,'Blake','Lisciandri','Coleman',52,8506863627,'blisciandri17@google.fr',6245058303,NULL),(58,'Carlie','Claasen','Esker',3,289421004,'cclaasen18@alexa.com',1854900536,NULL),(59,'Giralda','Whilder','Loftsgordon',35,3005020797,'gwhilder19@joomla.org',4059806043,NULL),(60,'Bond','Gait','Derek',3,5883700667,'bgait1a@google.ru',4024400870,NULL),(61,'Asa','Streight','Dottie',53,718900715,'astreight1b@cnn.com',2532528712,NULL),(62,'Delaney','Bexon','6th',623,112914187,'dbexon1c@livejournal.com',8891298138,NULL),(63,'Arlin','Westmorland','Luster',5,6393198761,'awestmorland1d@cornell.edu',1633522699,NULL);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_pedido`
--

DROP TABLE IF EXISTS `detalle_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_pedido` (
  `codigo_producto` int NOT NULL,
  `codigo_pedido` int NOT NULL,
  `cantidad_producto` int NOT NULL,
  `precio_producto` int NOT NULL,
  KEY `codigo_idx` (`codigo_producto`),
  KEY `id_pedido_idx` (`codigo_pedido`),
  CONSTRAINT `codigo` FOREIGN KEY (`codigo_producto`) REFERENCES `producto` (`codigo`),
  CONSTRAINT `id_pedido` FOREIGN KEY (`codigo_pedido`) REFERENCES `pedido` (`id_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_pedido`
--

LOCK TABLES `detalle_pedido` WRITE;
/*!40000 ALTER TABLE `detalle_pedido` DISABLE KEYS */;
INSERT INTO `detalle_pedido` VALUES (1,1,2,851),(3,1,3,4200),(2,1,1,270),(6,2,5,408),(8,2,12,1755),(3,3,5,4200),(1,3,6,851),(7,3,7,4913),(1,4,10,851),(1,4,2,851),(1,11,3,851),(3,11,5,4200),(5,11,2,639),(4,12,3,333),(2,12,4,270),(6,12,1,408),(2,17,1,270),(3,17,7,4200),(4,22,5,333),(4,23,5,333),(2,23,5,270),(8,24,5,1755),(5,24,10,639),(17,24,2,828),(16,25,1,828),(9,25,1,739),(16,26,2,828);
/*!40000 ALTER TABLE `detalle_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `id_empleado` int NOT NULL AUTO_INCREMENT,
  `nom_empleado` varchar(45) NOT NULL,
  `ap_empleado` varchar(45) NOT NULL,
  `dni_empleado` int NOT NULL,
  `calle_empleado` varchar(45) NOT NULL,
  `ncalle_empleado` int NOT NULL,
  `correo_empleado` varchar(50) NOT NULL,
  `cargo_empleado` int NOT NULL,
  `sucursal_empleado` int NOT NULL,
  PRIMARY KEY (`id_empleado`),
  UNIQUE KEY `dni_empleado_UNIQUE` (`dni_empleado`),
  UNIQUE KEY `correo_empleado_UNIQUE` (`correo_empleado`),
  KEY `id_sucursal_idx` (`sucursal_empleado`),
  KEY `id_cargo_idx` (`cargo_empleado`),
  CONSTRAINT `id_cargo` FOREIGN KEY (`cargo_empleado`) REFERENCES `puestos` (`id_puesto`),
  CONSTRAINT `id_sucursal` FOREIGN KEY (`sucursal_empleado`) REFERENCES `sucursal` (`idsucursal`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES (1,'juan ','martinez',24533595,'san juan',5463,'juanmartinez1@gmail.com',1,1),(2,'martina ','rodriguez',38055486,'salta',57,'martinarodriguez2@gmail.com',2,1),(3,'sebastian ','lopez',41654823,'san luis',897,'sebastianlopez3@gmail.com',3,1),(4,'valentina ','perez',31244564,'valentin alsina',236,'valentinaperez4@gmail.com',4,2),(5,'juan carlos ','ramirez',22533797,'libertad',674,'juancarlosramirez5@gmail.com',5,2),(6,'sofia ','garcia',33453124,'fucsias',234,'sofiagarcia6@gmail.com',6,2),(7,'mateo ','fernandez',42067554,'colombia',967,'mateofernandez7@gmail.com',7,3),(8,'isabella ','martinez',44536826,'españa',705,'isabellamartinez8@gmail.com',8,3),(9,'alejandro ','torres',40123345,'luzuriaga',234,'alejandrotorres9@gmail.com',9,3),(10,'camila ','gonzales',39355982,'san lorenzo',33,'camilagonzales10@gmail.com',10,1);
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marcas`
--

DROP TABLE IF EXISTS `marcas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marcas` (
  `id_marcas` int NOT NULL AUTO_INCREMENT,
  `nombre_marca` varchar(45) NOT NULL,
  PRIMARY KEY (`id_marcas`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marcas`
--

LOCK TABLES `marcas` WRITE;
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` VALUES (1,'Bimbo'),(2,'Coca-Cola'),(3,'La Serenisima'),(4,'Natura'),(5,'Oreo'),(6,'Paladini'),(7,'Pantene'),(8,'Paty'),(9,'Sin marca'),(10,'Skip');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medio_pago`
--

DROP TABLE IF EXISTS `medio_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medio_pago` (
  `id_medio_pago` int NOT NULL AUTO_INCREMENT,
  `tipo_medio_pago` varchar(45) NOT NULL,
  PRIMARY KEY (`id_medio_pago`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medio_pago`
--

LOCK TABLES `medio_pago` WRITE;
/*!40000 ALTER TABLE `medio_pago` DISABLE KEYS */;
INSERT INTO `medio_pago` VALUES (1,'efectivo'),(2,'transferencia'),(3,'debito'),(4,'credito');
/*!40000 ALTER TABLE `medio_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedido` (
  `id_pedido` int NOT NULL AUTO_INCREMENT,
  `estado_pedido` enum('en proceso','enviado','entregado') NOT NULL,
  `cliente_pedido` int NOT NULL,
  `num_factura_pedido` int NOT NULL,
  `sucursal_pedido` int NOT NULL,
  PRIMARY KEY (`id_pedido`),
  KEY `id_cliente_idx` (`cliente_pedido`),
  KEY `num_factura_idx` (`num_factura_pedido`),
  KEY `id_sucursal_idx` (`sucursal_pedido`),
  CONSTRAINT `id_cliente` FOREIGN KEY (`cliente_pedido`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `id_factura` FOREIGN KEY (`num_factura_pedido`) REFERENCES `venta` (`num_factura`),
  CONSTRAINT `sucursal` FOREIGN KEY (`sucursal_pedido`) REFERENCES `sucursal` (`idsucursal`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
INSERT INTO `pedido` VALUES (1,'en proceso',1,6,1),(2,'enviado',2,10,2),(3,'entregado',1,5,1),(4,'entregado',6,9,3),(5,'enviado',9,1,3),(6,'en proceso',8,2,1),(7,'enviado',5,8,2),(8,'entregado',10,4,1),(9,'en proceso',7,3,3),(10,'enviado',3,7,2),(11,'en proceso',1,18,3),(12,'en proceso',8,19,3),(13,'en proceso',1,20,1),(14,'en proceso',1,21,1),(15,'en proceso',1,22,3),(16,'en proceso',1,23,3),(17,'en proceso',1,24,2),(18,'en proceso',1,25,2),(19,'en proceso',1,26,3),(20,'en proceso',1,27,1),(21,'en proceso',1,28,1),(22,'en proceso',1,29,2),(23,'en proceso',1,30,1),(24,'en proceso',1,31,1),(25,'en proceso',8,32,2),(26,'en proceso',8,33,2);
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `codigo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `precio` float NOT NULL,
  `cantidad` int NOT NULL,
  `marca` int NOT NULL,
  `categoria_producto` int NOT NULL,
  `proveedor_producto` int NOT NULL,
  `tamaño` float NOT NULL,
  `um_producto` int NOT NULL,
  `img_producto` varchar(60) NOT NULL,
  `vendidos` int DEFAULT NULL,
  `estado` int DEFAULT NULL,
  PRIMARY KEY (`codigo`),
  KEY `id_proveedor_idx` (`proveedor_producto`),
  KEY `id_marca_idx` (`marca`),
  KEY `id_categoria_idx` (`categoria_producto`),
  KEY `id_medida_idx` (`um_producto`),
  CONSTRAINT `id_categoria` FOREIGN KEY (`categoria_producto`) REFERENCES `categoria` (`id_categoria`),
  CONSTRAINT `id_marca` FOREIGN KEY (`marca`) REFERENCES `marcas` (`id_marcas`),
  CONSTRAINT `id_medida` FOREIGN KEY (`um_producto`) REFERENCES `unidad_medida` (`id_medida`),
  CONSTRAINT `id_proveedor` FOREIGN KEY (`proveedor_producto`) REFERENCES `proveedor` (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'gaseosa cola',850.5,1000,2,2,1,2.5,4,'coca.webp',10,1),(2,'yogurt ',270,495,3,6,4,190,2,'yogurt.webp',5,1),(3,'milanesa nalga',4200,250,9,3,5,1,3,'milanesa.webp',NULL,1),(4,'galletas',333.4,1090,5,10,9,118,2,'oreo.webp',25,1),(5,'bananas',639,290,9,11,2,1,3,'banana.webp',13,0),(6,'mayonesa',408,1500,4,1,3,500,1,'mayonesa.webp',2,1),(7,'jamon cocido',4912.92,300,6,5,6,1,3,'jamon.jpg',NULL,1),(8,'shampoo',1755.01,1995,7,9,7,400,5,'pantene.webp',5,1),(9,'hamburguesa carne',739.03,2999,8,4,10,274,2,'paty.webp',5,1),(10,'jabon ropa',2890.08,2000,10,7,7,3,4,'jabon.webp',NULL,1),(11,'pan blanco',845.55,1000,1,8,8,550,2,'pan.webp',NULL,1),(16,'Sprite Lima Limon',828,197,2,2,1,2,4,'sprite.webp',15,1),(17,'Fanta Naranja',828,998,2,2,1,2,4,'fanta.webp',8,0);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  `nom_proveedor` varchar(45) NOT NULL,
  `ap_proveedor` varchar(45) DEFAULT NULL,
  `telefono_proveedor` bigint NOT NULL,
  `calle_proveedor` varchar(45) NOT NULL,
  `ncalle_proveedor` varchar(45) DEFAULT NULL,
  `correo_proveedor` varchar(50) NOT NULL,
  PRIMARY KEY (`id_proveedor`),
  UNIQUE KEY `correo_proveedor_UNIQUE` (`correo_proveedor`),
  UNIQUE KEY `telefono_proveedor_UNIQUE` (`telefono_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'juan ','gomez',2604551200,'rivadavia ','1500','juangomez55@gmail.com'),(2,'maria Elena ','rodriguez',2604551001,'olascoaga ','123','mariarodriguez1@gmail.com'),(3,'juan  ','lopez',2604551002,'santiago del estero   ','422','pedrolopez2@gmail.com'),(4,'ana ','martinez',2604551003,'san martin ','921','anamartinez3@gmail.com'),(5,'luis ','perez',2604551004,'paunero ','555','luisperez4@gmail.com'),(6,'laura ','garcia',2604551005,'rawson ','847','lauragarcia5@gmail.com'),(7,'diego ','fernandez',2604551006,'san juan ','200','diegofernandez6@gmail.com'),(8,'sofia ','diaz',2604551007,'matienzo ','1279','sofiadiaz7@gmail.com'),(9,'carlos ','sanchez',2604551008,'anglat ','881','carlossanchez8@gmail.com'),(10,'elena ','ramirez',2604551009,'uriburu ','430','elenaramirez9@gmail.com');
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puestos`
--

DROP TABLE IF EXISTS `puestos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puestos` (
  `id_puesto` int NOT NULL AUTO_INCREMENT,
  `nombre_puesto` varchar(45) NOT NULL,
  PRIMARY KEY (`id_puesto`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puestos`
--

LOCK TABLES `puestos` WRITE;
/*!40000 ALTER TABLE `puestos` DISABLE KEYS */;
INSERT INTO `puestos` VALUES (1,'Cajero'),(2,'Repositor'),(3,'Gerente'),(4,'Supervisor'),(5,'Seguridad'),(6,'Carnicero'),(7,'Panadero'),(8,'Verdulero'),(9,'Limpieza'),(10,'Recursos humanos');
/*!40000 ALTER TABLE `puestos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sucursal`
--

DROP TABLE IF EXISTS `sucursal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sucursal` (
  `idsucursal` int NOT NULL AUTO_INCREMENT,
  `direccion_sucursal` varchar(45) NOT NULL,
  `telefono_sucursal` bigint NOT NULL,
  `imagen_sucursal` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`idsucursal`),
  UNIQUE KEY `direccion_sucursal_UNIQUE` (`direccion_sucursal`),
  UNIQUE KEY `telefono_sucursal_UNIQUE` (`telefono_sucursal`),
  UNIQUE KEY `imagen_sucursal_UNIQUE` (`imagen_sucursal`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sucursal`
--

LOCK TABLES `sucursal` WRITE;
/*!40000 ALTER TABLE `sucursal` DISABLE KEYS */;
INSERT INTO `sucursal` VALUES (1,'san martin 550',2604579488,'edificio1.png'),(2,'rivadavia 1234',2604124355,'edificio2.png'),(3,'iselin 833',2604095889,'edificio3.png');
/*!40000 ALTER TABLE `sucursal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unidad_medida`
--

DROP TABLE IF EXISTS `unidad_medida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unidad_medida` (
  `id_medida` int NOT NULL AUTO_INCREMENT,
  `nombre_medida` varchar(45) NOT NULL,
  `siglas` varchar(45) NOT NULL,
  PRIMARY KEY (`id_medida`),
  UNIQUE KEY `siglas_UNIQUE` (`siglas`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidad_medida`
--

LOCK TABLES `unidad_medida` WRITE;
/*!40000 ALTER TABLE `unidad_medida` DISABLE KEYS */;
INSERT INTO `unidad_medida` VALUES (1,'centimetros cubicos','cm3'),(2,'gramos','g'),(3,'kilos','kg'),(4,'litros','l'),(5,'mililitros','ml');
/*!40000 ALTER TABLE `unidad_medida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `num_factura` int NOT NULL AUTO_INCREMENT,
  `fecha_venta` datetime NOT NULL,
  `total_venta` float NOT NULL,
  `medio_pago_venta` int NOT NULL,
  PRIMARY KEY (`num_factura`),
  KEY `id_medio_pago_idx` (`medio_pago_venta`),
  CONSTRAINT `id_medio_pago` FOREIGN KEY (`medio_pago_venta`) REFERENCES `medio_pago` (`id_medio_pago`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (1,'2023-08-30 00:00:00',5300,1),(2,'2023-09-01 00:00:00',12551.5,3),(3,'2023-09-01 00:00:00',7070.1,1),(4,'2023-09-01 00:00:00',10551.5,4),(5,'2023-09-02 00:00:00',3340,1),(6,'2023-09-02 00:00:00',1234.98,2),(7,'2023-09-02 00:00:00',68450.8,3),(8,'2023-09-02 00:00:00',42654.1,4),(9,'2023-09-03 00:00:00',1059.9,1),(10,'2023-09-03 00:00:00',500,1),(11,'2023-10-19 00:00:00',123,1),(14,'2023-10-19 00:00:00',270,4),(15,'2023-10-19 23:55:35',4954.5,2),(16,'2023-10-21 20:59:15',32295.1,3),(17,'2023-10-25 21:52:34',6022.9,2),(18,'2023-10-25 21:55:40',5689.5,1),(19,'2023-10-25 21:57:45',1011.4,4),(20,'2023-10-26 20:14:05',42000,1),(21,'2023-10-26 20:18:53',42000,2),(22,'2023-10-26 20:31:51',1120.5,2),(23,'2023-10-26 20:32:51',3787.7,2),(24,'2023-10-26 20:38:43',29670,4),(25,'2023-10-29 16:28:31',2207,2),(26,'2023-10-29 16:33:23',2747,2),(27,'2023-10-29 16:39:24',3017,3),(28,'2023-10-29 16:41:31',2477,2),(29,'2023-10-29 16:47:32',3017,3),(30,'2023-10-29 16:53:22',3017,3),(31,'2023-10-29 17:06:02',16821.1,4),(32,'2023-10-30 15:57:12',1567.03,2),(33,'2023-10-30 15:58:20',1656,2);
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-30 19:03:30
