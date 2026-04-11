-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 11/04/2026 às 16:25
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
-- Banco de dados: `inventario_pecas`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `pecas`
--

CREATE TABLE `pecas` (
  `id` int(11) NOT NULL,
  `codigo` varchar(20) DEFAULT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `veiculo` varchar(50) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  `quantidade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `pecas`
--

INSERT INTO `pecas` (`id`, `codigo`, `nome`, `veiculo`, `categoria`, `preco`, `quantidade`) VALUES
(1, 'GOL-MOT-001', 'Filtro de Óleo', 'Gol Quadrado', 'Motor', 25.90, 15),
(2, 'GOL-MOT-002', 'Vela de Ignição', 'Gol Quadrado', 'Motor', 12.50, 40),
(3, 'GOL-SUS-001', 'Amortecedor Dianteiro', 'Gol Quadrado', 'Suspensão', 189.00, 6),
(4, 'GOL-FRE-001', 'Pastilha de Freio', 'Gol Quadrado', 'Freios', 55.00, 20),
(5, 'GOL-ELE-001', 'Bateria 45Ah', 'Gol Quadrado', 'Elétrica', 320.00, 3),
(6, 'GOL-ELE-002', 'Alternador', 'Gol Quadrado', 'Elétrica', 450.00, 2),
(7, 'GOL-TRA-001', 'Cabo de Embreagem', 'Gol Quadrado', 'Transmissão', 38.00, 8),
(8, 'GOL-CAR-001', 'Carburador', 'Gol Quadrado', 'Carburação', 280.00, 4),
(9, 'teste', 'teste', 'Gol Quadrado', 'Geral', 25.00, 50);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `pecas`
--
ALTER TABLE `pecas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `pecas`
--
ALTER TABLE `pecas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
