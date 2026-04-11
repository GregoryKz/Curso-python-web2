-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 14/03/2026 às 12:41
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bliotecatitov1`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `realiza_emprestimo`
--

CREATE TABLE `realiza_emprestimo` (
  `fk_cliente` int(11) NOT NULL,
  `fk_emprestimo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `realiza_emprestimo`
--
ALTER TABLE `realiza_emprestimo`
  ADD PRIMARY KEY (`fk_cliente`,`fk_emprestimo`),
  ADD KEY `fk_emprestimo` (`fk_emprestimo`);

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `realiza_emprestimo`
--
ALTER TABLE `realiza_emprestimo`
  ADD CONSTRAINT `realiza_emprestimo_ibfk_1` FOREIGN KEY (`fk_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE CASCADE,
  ADD CONSTRAINT `realiza_emprestimo_ibfk_2` FOREIGN KEY (`fk_emprestimo`) REFERENCES `emprestimo` (`id_emprestimo`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
