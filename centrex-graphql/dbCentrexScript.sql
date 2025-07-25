USE [master]
GO
/****** Object:  Database [dbCentrex]    Script Date: 17/7/2025 14:18:31 ******/
CREATE DATABASE [dbCentrex]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'dbCentrex', FILENAME = N'Q:\SQL_DB\2017\Data\dbCentrex.mdf' , SIZE = 232000KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'dbCentrex_log', FILENAME = N'Q:\SQL_DB\2017\Data\dbCentrex_log.ldf' , SIZE = 636928KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO
ALTER DATABASE [dbCentrex] SET COMPATIBILITY_LEVEL = 110
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [dbCentrex].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [dbCentrex] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [dbCentrex] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [dbCentrex] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [dbCentrex] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [dbCentrex] SET ARITHABORT OFF 
GO
ALTER DATABASE [dbCentrex] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [dbCentrex] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [dbCentrex] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [dbCentrex] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [dbCentrex] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [dbCentrex] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [dbCentrex] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [dbCentrex] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [dbCentrex] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [dbCentrex] SET  DISABLE_BROKER 
GO
ALTER DATABASE [dbCentrex] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [dbCentrex] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [dbCentrex] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [dbCentrex] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [dbCentrex] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [dbCentrex] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [dbCentrex] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [dbCentrex] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [dbCentrex] SET  MULTI_USER 
GO
ALTER DATABASE [dbCentrex] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [dbCentrex] SET DB_CHAINING OFF 
GO
ALTER DATABASE [dbCentrex] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [dbCentrex] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
ALTER DATABASE [dbCentrex] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [dbCentrex] SET QUERY_STORE = OFF
GO
USE [dbCentrex]
GO
/****** Object:  User [javierp]    Script Date: 17/7/2025 14:18:31 ******/
CREATE USER [javierp] WITHOUT LOGIN WITH DEFAULT_SCHEMA=[javierp]
GO
/****** Object:  User [BRUNO\Facturar]    Script Date: 17/7/2025 14:18:31 ******/
CREATE USER [BRUNO\Facturar] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [javierp]
GO
ALTER ROLE [db_backupoperator] ADD MEMBER [BRUNO\Facturar]
GO
ALTER ROLE [db_datareader] ADD MEMBER [BRUNO\Facturar]
GO
ALTER ROLE [db_datawriter] ADD MEMBER [BRUNO\Facturar]
GO
/****** Object:  Schema [javierp]    Script Date: 17/7/2025 14:18:31 ******/
CREATE SCHEMA [javierp]
GO
/****** Object:  UserDefinedFunction [dbo].[CalculoComprobante]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[CalculoComprobante] 
(
	@nombreAbreviado NVARCHAR(10)
	, @puntoVenta INTEGER
	, @numeroComprobante INTEGER
)
	RETURNS NVARCHAR(50)
	BEGIN	
	RETURN CONCAT(@nombreAbreviado, ' Nº  ', REPLICATE('0', 4 - LEN(@puntoVenta)), @puntoVenta, '-', REPLICATE('0', 8 - LEN(@numeroComprobante)), @numeroComprobante)
	END
GO
/****** Object:  UserDefinedFunction [dbo].[CantidadConLetra]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE FUNCTION [dbo].[CantidadConLetra]
(
    @Numero             Decimal(18,2)
)
RETURNS Varchar(180)
AS
BEGIN
    DECLARE @ImpLetra Varchar(180)
        DECLARE @lnEntero bigint,
                        @lcRetorno VARCHAR(512),
                        @lnTerna bigint,
                        @lcMiles VARCHAR(512),
                        @lcCadena VARCHAR(512),
                        @lnUnidades bigint,
                        @lnDecenas bigint,
                        @lnCentenas bigint,
                        @lnFraccion bigint
        SELECT  @lnEntero = CAST(@Numero AS bigint),
                        @lnFraccion = (@Numero - @lnEntero) * 100,
                        @lcRetorno = '',
                        @lnTerna = 1
  WHILE @lnEntero > 0
  BEGIN /* WHILE */
            -- Recorro terna por terna
            SELECT @lcCadena = ''
            SELECT @lnUnidades = @lnEntero % 10
            SELECT @lnEntero = CAST(@lnEntero/10 AS bigint)
            SELECT @lnDecenas = @lnEntero % 10
            SELECT @lnEntero = CAST(@lnEntero/10 AS bigint)
            SELECT @lnCentenas = @lnEntero % 10
            SELECT @lnEntero = CAST(@lnEntero/10 AS bigint)
            -- Analizo las unidades
            SELECT @lcCadena =
            CASE /* UNIDADES */
              WHEN @lnUnidades = 1 THEN 'UN ' + @lcCadena
              WHEN @lnUnidades = 2 THEN 'DOS ' + @lcCadena
              WHEN @lnUnidades = 3 THEN 'TRES ' + @lcCadena
              WHEN @lnUnidades = 4 THEN 'CUATRO ' + @lcCadena
              WHEN @lnUnidades = 5 THEN 'CINCO ' + @lcCadena
              WHEN @lnUnidades = 6 THEN 'SEIS ' + @lcCadena
              WHEN @lnUnidades = 7 THEN 'SIETE ' + @lcCadena
              WHEN @lnUnidades = 8 THEN 'OCHO ' + @lcCadena
              WHEN @lnUnidades = 9 THEN 'NUEVE ' + @lcCadena
              ELSE @lcCadena
            END /* UNIDADES */
            -- Analizo las decenas
            SELECT @lcCadena =
            CASE /* DECENAS */
              WHEN @lnDecenas = 1 THEN
                CASE @lnUnidades
                  WHEN 0 THEN 'DIEZ '
                  WHEN 1 THEN 'ONCE '
                  WHEN 2 THEN 'DOCE '
                  WHEN 3 THEN 'TRECE '
                  WHEN 4 THEN 'CATORCE '
                  WHEN 5 THEN 'QUINCE '
                  WHEN 6 THEN 'DIECISEIS '
                  WHEN 7 THEN 'DIECISIETE '
                  WHEN 8 THEN 'DIECIOCHO '
                  WHEN 9 THEN 'DIECINUEVE '
                END
              WHEN @lnDecenas = 2 THEN
              CASE @lnUnidades
                WHEN 0 THEN 'VEINTE '
                ELSE 'VEINTI' + @lcCadena
              END
              WHEN @lnDecenas = 3 THEN
              CASE @lnUnidades
                WHEN 0 THEN 'TREINTA '
                ELSE 'TREINTA Y ' + @lcCadena
              END
              WHEN @lnDecenas = 4 THEN
                CASE @lnUnidades
                    WHEN 0 THEN 'CUARENTA'
                    ELSE 'CUARENTA Y ' + @lcCadena
                END
              WHEN @lnDecenas = 5 THEN
                CASE @lnUnidades
                    WHEN 0 THEN 'CINCUENTA '
                    ELSE 'CINCUENTA Y ' + @lcCadena
                END
              WHEN @lnDecenas = 6 THEN
                CASE @lnUnidades
                    WHEN 0 THEN 'SESENTA '
                    ELSE 'SESENTA Y ' + @lcCadena
                END
              WHEN @lnDecenas = 7 THEN
                 CASE @lnUnidades
                    WHEN 0 THEN 'SETENTA '
                    ELSE 'SETENTA Y ' + @lcCadena
                 END
              WHEN @lnDecenas = 8 THEN
                CASE @lnUnidades
                    WHEN 0 THEN 'OCHENTA '
                    ELSE  'OCHENTA Y ' + @lcCadena
                END
              WHEN @lnDecenas = 9 THEN
                CASE @lnUnidades
                    WHEN 0 THEN 'NOVENTA '
                    ELSE 'NOVENTA Y ' + @lcCadena
                END
              ELSE @lcCadena
            END /* DECENAS */
            -- Analizo las centenas
            SELECT @lcCadena =
            CASE /* CENTENAS */
              WHEN @lnCentenas = 1 THEN 'CIENTO ' + @lcCadena
              WHEN @lnCentenas = 2 THEN 'DOSCIENTOS ' + @lcCadena
              WHEN @lnCentenas = 3 THEN 'TRESCIENTOS ' + @lcCadena
              WHEN @lnCentenas = 4 THEN 'CUATROCIENTOS ' + @lcCadena
              WHEN @lnCentenas = 5 THEN 'QUINIENTOS ' + @lcCadena
              WHEN @lnCentenas = 6 THEN 'SEISCIENTOS ' + @lcCadena
              WHEN @lnCentenas = 7 THEN 'SETECIENTOS ' + @lcCadena
              WHEN @lnCentenas = 8 THEN 'OCHOCIENTOS ' + @lcCadena
              WHEN @lnCentenas = 9 THEN 'NOVECIENTOS ' + @lcCadena
              ELSE @lcCadena
            END /* CENTENAS */
            -- Analizo la terna
            SELECT @lcCadena =
            CASE /* TERNA */
              WHEN @lnTerna = 1 THEN @lcCadena
              WHEN @lnTerna = 2 THEN @lcCadena + 'MIL '
              WHEN @lnTerna = 3 THEN @lcCadena + 'MILLONES '
              WHEN @lnTerna = 4 THEN @lcCadena + 'MIL '
              ELSE ''
            END /* TERNA */
            -- Armo el retorno terna a terna
            SELECT @lcRetorno = @lcCadena  + @lcRetorno
            SELECT @lnTerna = @lnTerna + 1
   END /* WHILE */
   IF @lnTerna = 1
       SELECT @lcRetorno = 'CERO'
   DECLARE @sFraccion VARCHAR(15)
   SET @sFraccion = '00' + LTRIM(CAST(@lnFraccion AS varchar))
   SELECT @ImpLetra = RTRIM(@lcRetorno) + ' PESOS ' + SUBSTRING(@sFraccion,LEN(@sFraccion)-1,2) + '/100'
   RETURN @ImpLetra
END
GO
/****** Object:  UserDefinedFunction [dbo].[idultimoingreso]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[idultimoingreso]()
RETURNS INT
AS
BEGIN
  DECLARE         @idingreso           INT

  SELECT TOP 1          @idingreso = id_ingreso
  FROM            registros_stock   
  ORDER BY id_ingreso DESC

   IF @idingreso IS NULL 
  BEGIN
	SET @idingreso = 1
  END

  RETURN @idingreso
END
GO
/****** Object:  UserDefinedFunction [dbo].[idUltimoPresupuesto]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[idUltimoPresupuesto]()
RETURNS INT
AS
BEGIN
  DECLARE         @idPresupuesto           INT

   SELECT @idPresupuesto = MAX(idPresupuesto)
	FROM pedidos

 IF @idPresupuesto IS NULL 
  BEGIN
	SET @idPresupuesto = 1
  END

  RETURN @idPresupuesto
END
GO
/****** Object:  UserDefinedFunction [dbo].[mascaraCUIT]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[mascaraCUIT](@cuit VARCHAR(50))
RETURNS VARCHAR(50)
AS
BEGIN
   IF LEN(@cuit) <  11 
	BEGIN
		RETURN @cuit
	END
	ELSE
	BEGIN
		SET @cuit = CONCAT(SUBSTRING(@cuit,1,2), '-', SUBSTRING(@cuit,3,8), '-', SUBSTRING(@cuit,11,1))		
	END

  RETURN @cuit
END
GO
/****** Object:  UserDefinedFunction [dbo].[milesArgentinos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[milesArgentinos](@valor VARCHAR(50))
RETURNS VARCHAR(50)
AS
BEGIN
   SET @valor = REPLACE(@valor, '.', '*')
  SET @valor = REPLACE(@valor, ',', '.')
  SET @valor = REPLACE(@valor, '*', ',')
  
  RETURN @valor
END
GO
/****** Object:  Table [dbo].[bancos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[bancos](
	[id_banco] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](100) NOT NULL,
	[id_pais] [int] NOT NULL,
	[n_banco] [int] NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_bancos] PRIMARY KEY CLUSTERED 
(
	[id_banco] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cuentas_bancarias]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cuentas_bancarias](
	[id_cuentaBancaria] [int] IDENTITY(1,1) NOT NULL,
	[id_banco] [int] NOT NULL,
	[nombre] [nvarchar](100) NOT NULL,
	[id_moneda] [int] NOT NULL,
	[saldo] [decimal](18, 3) NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_cuentas_bancarias_1] PRIMARY KEY CLUSTERED 
(
	[id_cuentaBancaria] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cheques]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cheques](
	[id_cheque] [int] IDENTITY(1,1) NOT NULL,
	[fecha_ingreso] [date] NOT NULL,
	[fecha_emision] [date] NOT NULL,
	[id_cliente] [int] NULL,
	[id_proveedor] [int] NULL,
	[id_banco] [int] NOT NULL,
	[nCheque] [int] NOT NULL,
	[nCheque2] [int] NOT NULL,
	[importe] [decimal](18, 3) NOT NULL,
	[id_estadoch] [int] NOT NULL,
	[fecha_cobro] [date] NULL,
	[fecha_salida] [date] NULL,
	[fecha_deposito] [date] NULL,
	[recibido] [bit] NULL,
	[emitido] [bit] NULL,
	[id_cuentaBancaria] [int] NULL,
	[eCheck] [bit] NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_cheques] PRIMARY KEY CLUSTERED 
(
	[id_cheque] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[cheques_a_cobrar]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [dbo].[cheques_a_cobrar]
AS
SELECT        dbo.cheques.fecha_cobro, dbo.cheques.importe, dbo.bancos.nombre AS banco, dbo.cuentas_bancarias.nombre AS cuenta_bancaria, dbo.cuentas_bancarias.saldo, DATEADD(DAY, 2, dbo.cheques.fecha_cobro) 
                         AS fecha_cobro_real, dbo.cheques.id_banco, dbo.cheques.id_cuentaBancaria, dbo.cheques.id_estadoch, dbo.cheques.id_cheque
FROM            dbo.cheques INNER JOIN
                         dbo.cuentas_bancarias ON dbo.cheques.id_cuentaBancaria = dbo.cuentas_bancarias.id_cuentaBancaria INNER JOIN
                         dbo.bancos ON dbo.cheques.id_banco = dbo.bancos.id_banco AND dbo.cuentas_bancarias.id_banco = dbo.bancos.id_banco
WHERE        (dbo.cheques.id_estadoch = 5) AND (DATEADD(DAY, 2, dbo.cheques.fecha_cobro) = CONVERT([date], GETDATE()))
GO
/****** Object:  Table [dbo].[ajustes_stock]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ajustes_stock](
	[id_ajusteStock] [int] IDENTITY(1,1) NOT NULL,
	[fecha] [date] NOT NULL,
	[id_item] [int] NOT NULL,
	[cantidad] [int] NOT NULL,
	[notas] [nvarchar](max) NULL,
 CONSTRAINT [PK_ajustes_stock] PRIMARY KEY CLUSTERED 
(
	[id_ajusteStock] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[asocItems]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[asocItems](
	[id_item] [int] NOT NULL,
	[id_item_asoc] [int] NOT NULL,
	[cantidad] [int] NOT NULL,
 CONSTRAINT [PK_asocItems] PRIMARY KEY CLUSTERED 
(
	[id_item] ASC,
	[id_item_asoc] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cajas]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cajas](
	[id_caja] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](50) NOT NULL,
	[esCC] [bit] NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_cajas] PRIMARY KEY CLUSTERED 
(
	[id_caja] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cambios]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cambios](
	[id_cambio] [int] IDENTITY(1,1) NOT NULL,
	[cambio] [varchar](max) NOT NULL,
	[fecha] [date] NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_cambios] PRIMARY KEY CLUSTERED 
(
	[id_cambio] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cc_clientes]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cc_clientes](
	[id_cc] [int] IDENTITY(1,1) NOT NULL,
	[id_cliente] [int] NOT NULL,
	[id_moneda] [int] NOT NULL,
	[nombre] [nvarchar](50) NOT NULL,
	[saldo] [decimal](18, 3) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_cc_clientes] PRIMARY KEY CLUSTERED 
(
	[id_cc] ASC,
	[id_cliente] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cc_proveedores]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cc_proveedores](
	[id_cc] [int] IDENTITY(1,1) NOT NULL,
	[id_proveedor] [int] NOT NULL,
	[id_moneda] [int] NOT NULL,
	[nombre] [nvarchar](50) NOT NULL,
	[saldo] [decimal](18, 3) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_cc_proveedores] PRIMARY KEY CLUSTERED 
(
	[id_cc] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[clientes]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[clientes](
	[id_cliente] [int] IDENTITY(1,1) NOT NULL,
	[taxNumber] [nvarchar](50) NULL,
	[razon_social] [nvarchar](100) NOT NULL,
	[nombre_fantasia] [nvarchar](100) NULL,
	[contacto] [nvarchar](100) NULL,
	[telefono] [nvarchar](50) NULL,
	[celular] [nvarchar](50) NULL,
	[email] [nvarchar](100) NULL,
	[id_provincia_fiscal] [int] NULL,
	[direccion_fiscal] [nvarchar](200) NULL,
	[localidad_fiscal] [nvarchar](200) NULL,
	[cp_fiscal] [nvarchar](20) NULL,
	[id_provincia_entrega] [int] NULL,
	[direccion_entrega] [nvarchar](200) NULL,
	[localidad_entrega] [nvarchar](200) NULL,
	[cp_entrega] [nvarchar](20) NULL,
	[notas] [nvarchar](max) NULL,
	[esInscripto] [bit] NOT NULL,
	[activo] [bit] NOT NULL,
	[id_tipoDocumento] [int] NOT NULL,
	[id_claseFiscal] [int] NULL,
 CONSTRAINT [PK__Table__677F38F5CAA705E3] PRIMARY KEY CLUSTERED 
(
	[id_cliente] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cobros]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cobros](
	[id_cobro] [int] IDENTITY(1,1) NOT NULL,
	[id_cobro_oficial] [int] NOT NULL,
	[id_cobro_no_oficial] [int] NOT NULL,
	[fecha_carga] [date] NOT NULL,
	[fecha_cobro] [date] NOT NULL,
	[id_cliente] [int] NOT NULL,
	[id_cc] [int] NOT NULL,
	[dineroEnCc] [decimal](18, 3) NOT NULL,
	[efectivo] [decimal](18, 3) NOT NULL,
	[totalTransferencia] [decimal](18, 3) NOT NULL,
	[totalCh] [decimal](18, 3) NOT NULL,
	[totalRetencion] [decimal](18, 3) NOT NULL,
	[total] [decimal](18, 3) NOT NULL,
	[hayCheque] [bit] NOT NULL,
	[hayTransferencia] [bit] NOT NULL,
	[hayRetencion] [bit] NOT NULL,
	[activo] [bit] NOT NULL,
	[id_anulaCobro] [int] NULL,
	[notas] [nvarchar](max) NULL,
	[firmante] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_cobros] PRIMARY KEY CLUSTERED 
(
	[id_cobro] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cobros_cheques]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cobros_cheques](
	[id_cobro] [int] NOT NULL,
	[id_cheque] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cobros_Nfacturas_importes]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cobros_Nfacturas_importes](
	[id_cobro] [int] NOT NULL,
	[fecha] [date] NOT NULL,
	[nfactura] [nvarchar](50) NOT NULL,
	[importe] [decimal](18, 6) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cobros_retenciones]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cobros_retenciones](
	[id_retencion] [int] IDENTITY(1,1) NOT NULL,
	[id_cobro] [int] NOT NULL,
	[id_impuesto] [int] NOT NULL,
	[total] [decimal](18, 3) NOT NULL,
	[notas] [nvarchar](max) NULL,
 CONSTRAINT [PK_cobros_retenciones] PRIMARY KEY CLUSTERED 
(
	[id_retencion] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[comprobantes]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[comprobantes](
	[id_comprobante] [int] IDENTITY(1,1) NOT NULL,
	[comprobante] [nvarchar](100) NOT NULL,
	[id_tipoComprobante] [int] NOT NULL,
	[numeroComprobante] [int] NOT NULL,
	[puntoVenta] [int] NOT NULL,
	[esFiscal] [bit] NULL,
	[esElectronica] [bit] NULL,
	[esManual] [bit] NULL,
	[esPresupuesto] [bit] NULL,
	[activo] [bit] NOT NULL,
	[testing] [bit] NOT NULL,
	[maxItems] [int] NULL,
	[comprobanteRelacionado] [int] NULL,
	[esMiPyME] [bit] NOT NULL,
	[CBU_emisor] [nvarchar](22) NULL,
	[alias_CBU_emisor] [nvarchar](50) NULL,
	[anula_MiPyME] [nvarchar](1) NULL,
	[contabilizar] [bit] NOT NULL,
	[mueveStock] [bit] NOT NULL,
	[id_modoMiPyme] [int] NOT NULL,
 CONSTRAINT [PK_comprobantes] PRIMARY KEY CLUSTERED 
(
	[id_comprobante] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[comprobantes_compras]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[comprobantes_compras](
	[id_comprobanteCompra] [int] IDENTITY(1,1) NOT NULL,
	[fecha_carga] [date] NOT NULL,
	[fecha_comprobante] [date] NOT NULL,
	[id_tipoComprobante] [int] NOT NULL,
	[id_proveedor] [int] NOT NULL,
	[id_cc] [int] NOT NULL,
	[id_moneda] [int] NOT NULL,
	[puntoVenta] [nvarchar](10) NULL,
	[numeroComprobante] [nvarchar](50) NULL,
	[id_condicion_compra] [int] NOT NULL,
	[subtotal] [decimal](18, 3) NULL,
	[impuestos] [decimal](18, 3) NULL,
	[conceptos] [decimal](18, 3) NULL,
	[total] [decimal](18, 3) NULL,
	[tasaCambio] [decimal](18, 3) NULL,
	[nota] [nvarchar](max) NULL,
	[cae] [nvarchar](50) NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_comprobantes_compras] PRIMARY KEY CLUSTERED 
(
	[id_comprobanteCompra] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[comprobantes_compras_conceptos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[comprobantes_compras_conceptos](
	[id_comprobanteCompraConcepto] [int] IDENTITY(1,1) NOT NULL,
	[id_comprobanteCompra] [int] NOT NULL,
	[id_concepto_compra] [int] NOT NULL,
	[subtotal] [decimal](18, 3) NOT NULL,
	[iva] [decimal](18, 3) NOT NULL,
	[total] [decimal](18, 3) NOT NULL,
 CONSTRAINT [PK_comprobantes_compras_conceptos] PRIMARY KEY CLUSTERED 
(
	[id_comprobanteCompraConcepto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[comprobantes_compras_impuestos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[comprobantes_compras_impuestos](
	[id_comprobanteCompraImpuesto] [int] IDENTITY(1,1) NOT NULL,
	[id_comprobanteCompra] [int] NOT NULL,
	[id_impuesto] [int] NOT NULL,
	[importe] [decimal](18, 3) NOT NULL,
 CONSTRAINT [PK_comprobantes_compras_impuestos] PRIMARY KEY CLUSTERED 
(
	[id_comprobanteCompraImpuesto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[comprobantes_compras_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[comprobantes_compras_items](
	[id_comprobanteCompraItem] [int] IDENTITY(1,1) NOT NULL,
	[id_comprobanteCompra] [int] NOT NULL,
	[id_item] [int] NOT NULL,
	[cantidad] [int] NOT NULL,
	[precio] [decimal](18, 2) NOT NULL,
 CONSTRAINT [PK_comprobantes_compras_items] PRIMARY KEY CLUSTERED 
(
	[id_comprobanteCompraItem] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[conceptos_compra]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[conceptos_compra](
	[id_concepto_compra] [int] IDENTITY(1,1) NOT NULL,
	[concepto] [nvarchar](100) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_conceptos_compra] PRIMARY KEY CLUSTERED 
(
	[id_concepto_compra] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[condiciones_compra]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[condiciones_compra](
	[id_condicion_compra] [int] IDENTITY(1,1) NOT NULL,
	[condicion] [nvarchar](100) NOT NULL,
	[vencimiento] [int] NOT NULL,
	[recargo] [decimal](18, 4) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_condiciones_compra] PRIMARY KEY CLUSTERED 
(
	[id_condicion_compra] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[consultas_personalizadas]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[consultas_personalizadas](
	[id_consulta] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](100) NOT NULL,
	[consulta] [nvarchar](max) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_consultas_personalizadas] PRIMARY KEY CLUSTERED 
(
	[id_consulta] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[empresa]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[empresa](
	[id_empresa] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](100) NOT NULL,
	[direccion] [nvarchar](max) NOT NULL,
	[cuit] [nvarchar](50) NOT NULL,
	[ingresos_brutos] [nvarchar](50) NULL,
	[inicio_actividades] [nvarchar](10) NULL,
	[logo] [image] NULL,
	[fecha] [date] NOT NULL,
 CONSTRAINT [PK_empresa] PRIMARY KEY CLUSTERED 
(
	[id_empresa] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[impuestos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[impuestos](
	[id_impuesto] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](100) NOT NULL,
	[esRetencion] [bit] NULL,
	[esPercepcion] [bit] NULL,
	[porcentaje] [decimal](18, 4) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_impuestos] PRIMARY KEY CLUSTERED 
(
	[id_impuesto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[items](
	[id_item] [int] IDENTITY(1,1) NOT NULL,
	[item] [nvarchar](50) NOT NULL,
	[descript] [nvarchar](54) NULL,
	[cantidad] [int] NULL,
	[costo] [decimal](18, 6) NOT NULL,
	[precio_lista] [decimal](18, 6) NOT NULL,
	[id_tipo] [int] NOT NULL,
	[id_marca] [int] NOT NULL,
	[id_proveedor] [int] NOT NULL,
	[factor] [decimal](18, 6) NULL,
	[esDescuento] [bit] NOT NULL,
	[esMarkup] [bit] NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_items] PRIMARY KEY CLUSTERED 
(
	[id_item] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[items_impuestos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[items_impuestos](
	[id_item] [int] NOT NULL,
	[id_impuesto] [int] NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_items_impuestos] PRIMARY KEY CLUSTERED 
(
	[id_item] ASC,
	[id_impuesto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[marcas_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[marcas_items](
	[id_marca] [int] IDENTITY(1,1) NOT NULL,
	[marca] [nvarchar](50) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_marcas_items] PRIMARY KEY CLUSTERED 
(
	[id_marca] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ordenes_compras]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ordenes_compras](
	[id_ordenCompra] [int] IDENTITY(1,1) NOT NULL,
	[id_proveedor] [int] NOT NULL,
	[fecha_carga] [date] NOT NULL,
	[fecha_comprobante] [date] NOT NULL,
	[fecha_recepcion] [date] NULL,
	[subtotal] [decimal](18, 3) NOT NULL,
	[iva] [decimal](18, 3) NOT NULL,
	[total] [decimal](18, 3) NOT NULL,
	[recibido] [bit] NULL,
	[notas] [nvarchar](max) NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_ordenes_compras] PRIMARY KEY CLUSTERED 
(
	[id_ordenCompra] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ordenesCompras_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ordenesCompras_items](
	[id_ocItem] [int] IDENTITY(1,1) NOT NULL,
	[id_item] [int] NOT NULL,
	[cantidad] [int] NOT NULL,
	[descript] [nvarchar](54) NULL,
	[cantidad_recibida] [int] NULL,
	[precio] [decimal](18, 3) NOT NULL,
	[id_ordenCompra] [int] NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_ordenesCompra_items] PRIMARY KEY CLUSTERED 
(
	[id_ocItem] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[pagos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pagos](
	[id_pago] [int] IDENTITY(1,1) NOT NULL,
	[fecha_carga] [date] NULL,
	[fecha_pago] [date] NOT NULL,
	[id_proveedor] [int] NOT NULL,
	[id_cc] [int] NOT NULL,
	[dineroEnCc] [decimal](18, 3) NOT NULL,
	[efectivo] [decimal](18, 3) NOT NULL,
	[totalTransferencia] [decimal](18, 3) NOT NULL,
	[totalCh] [decimal](18, 0) NOT NULL,
	[total] [decimal](18, 3) NOT NULL,
	[hayCheque] [bit] NOT NULL,
	[hayTransferencia] [bit] NOT NULL,
	[activo] [bit] NOT NULL,
	[id_anulaPago] [int] NULL,
	[notas] [nvarchar](max) NULL,
 CONSTRAINT [PK_pagos] PRIMARY KEY CLUSTERED 
(
	[id_pago] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[pagos_cheques]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pagos_cheques](
	[id_pago] [int] NOT NULL,
	[id_cheque] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[pagos_nFacturas_importes]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pagos_nFacturas_importes](
	[id_pago] [int] NOT NULL,
	[fecha] [date] NOT NULL,
	[nfactura] [nvarchar](50) NOT NULL,
	[importe] [decimal](18, 3) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[paises]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[paises](
	[id_pais] [int] IDENTITY(1,1) NOT NULL,
	[pais] [nvarchar](100) NOT NULL,
 CONSTRAINT [PK_paises] PRIMARY KEY CLUSTERED 
(
	[id_pais] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[pedidos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pedidos](
	[id_pedido] [int] IDENTITY(1,1) NOT NULL,
	[fecha] [date] NOT NULL,
	[fecha_edicion] [date] NOT NULL,
	[id_cliente] [int] NOT NULL,
	[markup] [decimal](18, 3) NULL,
	[subtotal] [decimal](18, 3) NOT NULL,
	[iva] [decimal](18, 3) NULL,
	[total] [decimal](18, 3) NOT NULL,
	[nota1] [nvarchar](200) NULL,
	[nota2] [nvarchar](200) NULL,
	[esPresupuesto] [bit] NOT NULL,
	[activo] [bit] NOT NULL,
	[cerrado] [bit] NOT NULL,
	[idPresupuesto] [int] NULL,
	[id_comprobante] [int] NOT NULL,
	[cae] [nvarchar](50) NULL,
	[fechaVencimiento_cae] [date] NULL,
	[puntoVenta] [int] NULL,
	[numeroComprobante] [int] NULL,
	[codigoDeBarras] [nvarchar](100) NULL,
	[esTest] [bit] NOT NULL,
	[id_cc] [int] NULL,
	[fc_qr] [varbinary](max) NULL,
	[numeroComprobante_anulado] [int] NULL,
	[numeroPedido_anulado] [int] NULL,
	[esDuplicado] [bit] NULL,
	[id_usuario] [int] NULL,
 CONSTRAINT [PK_pedidos] PRIMARY KEY CLUSTERED 
(
	[id_pedido] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[pedidos_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pedidos_items](
	[id_pedidoItem] [int] IDENTITY(1,1) NOT NULL,
	[id_item] [int] NULL,
	[cantidad] [int] NOT NULL,
	[precio] [decimal](18, 2) NOT NULL,
	[id_pedido] [int] NULL,
	[activo] [bit] NOT NULL,
	[descript] [nvarchar](100) NULL,
 CONSTRAINT [PK_pedidos_items_1] PRIMARY KEY CLUSTERED 
(
	[id_pedidoItem] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[perfiles]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[perfiles](
	[id_perfil] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](50) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_perfiles] PRIMARY KEY CLUSTERED 
(
	[id_perfil] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[permisos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[permisos](
	[id_permiso] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_permisos] PRIMARY KEY CLUSTERED 
(
	[id_permiso] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[permisos_perfiles]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[permisos_perfiles](
	[id_permiso] [int] NOT NULL,
	[id_pefil] [int] NOT NULL,
 CONSTRAINT [PK_permisos_perfiles] PRIMARY KEY CLUSTERED 
(
	[id_permiso] ASC,
	[id_pefil] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[produccion]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[produccion](
	[id_produccion] [int] IDENTITY(1,1) NOT NULL,
	[id_proveedor] [int] NOT NULL,
	[fecha_carga] [date] NOT NULL,
	[fecha_envio] [date] NULL,
	[fecha_recepcion] [date] NULL,
	[enviado] [bit] NULL,
	[recibido] [bit] NULL,
	[notas] [nvarchar](max) NULL,
	[activo] [bit] NOT NULL,
	[id_usuario] [int] NOT NULL,
 CONSTRAINT [PK_produccion] PRIMARY KEY CLUSTERED 
(
	[id_produccion] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[produccion_asocItems]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[produccion_asocItems](
	[id_produccion] [int] NOT NULL,
	[id_item] [int] NOT NULL,
	[id_item_asoc] [int] NOT NULL,
	[cantidad_item_asoc_enviada] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[produccion_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[produccion_items](
	[id_produccionItem] [int] IDENTITY(1,1) NOT NULL,
	[id_produccion] [int] NOT NULL,
	[id_item] [int] NOT NULL,
	[cantidad] [int] NOT NULL,
	[id_item_recibido] [int] NULL,
	[cantidad_recibida] [int] NULL,
	[descript] [nvarchar](100) NULL,
	[activo] [bit] NULL,
 CONSTRAINT [PK_produccion_items] PRIMARY KEY CLUSTERED 
(
	[id_produccionItem] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[proveedores]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[proveedores](
	[id_proveedor] [int] IDENTITY(1,1) NOT NULL,
	[taxNumber] [nvarchar](50) NULL,
	[razon_social] [nvarchar](100) NOT NULL,
	[contacto] [nvarchar](100) NULL,
	[telefono] [nvarchar](50) NULL,
	[celular] [nvarchar](50) NULL,
	[email] [nvarchar](100) NULL,
	[id_provincia_fiscal] [int] NULL,
	[direccion_fiscal] [nvarchar](200) NULL,
	[localidad_fiscal] [nvarchar](200) NULL,
	[cp_fiscal] [nvarchar](20) NULL,
	[id_provincia_entrega] [int] NULL,
	[direccion_entrega] [nvarchar](200) NULL,
	[localidad_entrega] [nvarchar](200) NULL,
	[cp_entrega] [nvarchar](20) NULL,
	[notas] [nvarchar](max) NULL,
	[esInscripto] [bit] NOT NULL,
	[vendedor] [nvarchar](100) NULL,
	[activo] [bit] NOT NULL,
	[id_tipoDocumento] [int] NOT NULL,
	[id_claseFiscal] [int] NULL,
 CONSTRAINT [PK_proveedores] PRIMARY KEY CLUSTERED 
(
	[id_proveedor] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[provincias]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[provincias](
	[id_provincia] [int] IDENTITY(1,1) NOT NULL,
	[id_pais] [int] NOT NULL,
	[provincia] [nvarchar](100) NOT NULL,
 CONSTRAINT [PK_provincias] PRIMARY KEY CLUSTERED 
(
	[id_provincia] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[registros_stock]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[registros_stock](
	[id_registro] [int] IDENTITY(1,1) NOT NULL,
	[id_ingreso] [int] NOT NULL,
	[fecha] [date] NULL,
	[fecha_ingreso] [date] NOT NULL,
	[factura] [nvarchar](50) NULL,
	[archivofc] [image] NULL,
	[id_proveedor] [int] NOT NULL,
	[id_item] [int] NOT NULL,
	[cantidad] [int] NOT NULL,
	[costo] [decimal](18, 2) NOT NULL,
	[precio_lista] [decimal](18, 2) NOT NULL,
	[factor] [decimal](18, 2) NOT NULL,
	[cantidad_anterior] [int] NOT NULL,
	[costo_anterior] [decimal](18, 2) NOT NULL,
	[precio_lista_anterior] [decimal](18, 2) NOT NULL,
	[factor_anterior] [decimal](18, 2) NOT NULL,
	[nota] [nvarchar](max) NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_registros_stock_1] PRIMARY KEY CLUSTERED 
(
	[id_registro] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[separador_decimal]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[separador_decimal](
	[id_separador] [int] IDENTITY(1,1) NOT NULL,
	[separador] [varchar](1) NOT NULL,
 CONSTRAINT [PK_separador_decimal] PRIMARY KEY CLUSTERED 
(
	[id_separador] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sys_claseComprobante]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sys_claseComprobante](
	[id_claseComprobante] [int] IDENTITY(1,1) NOT NULL,
	[descript] [nvarchar](100) NOT NULL,
 CONSTRAINT [PK_sys_claseComprobante] PRIMARY KEY CLUSTERED 
(
	[id_claseComprobante] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sys_ClasesFiscales]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sys_ClasesFiscales](
	[id_claseFiscal] [int] IDENTITY(1,1) NOT NULL,
	[descript] [nvarchar](100) NOT NULL,
 CONSTRAINT [PK_sys_ClasesFiscales] PRIMARY KEY CLUSTERED 
(
	[id_claseFiscal] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sys_modoMiPyme]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sys_modoMiPyme](
	[id_modoMiPyme] [int] IDENTITY(1,1) NOT NULL,
	[modo] [nvarchar](100) NOT NULL,
	[abreviatura] [nvarchar](10) NOT NULL,
 CONSTRAINT [PK_sys:_modoMiPyme] PRIMARY KEY CLUSTERED 
(
	[id_modoMiPyme] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sysestados_cheques]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sysestados_cheques](
	[id_estadoch] [int] IDENTITY(1,1) NOT NULL,
	[estado] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_sysestados_cheques] PRIMARY KEY CLUSTERED 
(
	[id_estadoch] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sysMoneda]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sysMoneda](
	[id_moneda] [int] IDENTITY(1,1) NOT NULL,
	[moneda] [nvarchar](5) NOT NULL,
 CONSTRAINT [PK_sysMoneda] PRIMARY KEY CLUSTERED 
(
	[id_moneda] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tipos_comprobantes]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tipos_comprobantes](
	[id_tipoComprobante] [int] NOT NULL,
	[comprobante_AFIP] [nvarchar](100) NOT NULL,
	[id_claseFiscal] [nvarchar](100) NULL,
	[signoProveedor] [char](1) NULL,
	[signoCliente] [char](1) NULL,
	[discriminaIVA] [bit] NULL,
	[esRemito] [bit] NULL,
	[nombreAbreviado] [nvarchar](10) NULL,
	[id_claseComprobante] [int] NOT NULL,
	[id_anulaTipoComprobante] [int] NULL,
	[contabilizar] [bit] NOT NULL,
 CONSTRAINT [PK_tipos_comprobantes] PRIMARY KEY CLUSTERED 
(
	[id_tipoComprobante] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tipos_documentos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tipos_documentos](
	[id_tipoDocumento] [int] NOT NULL,
	[documento] [nvarchar](50) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_tipos_documentos] PRIMARY KEY CLUSTERED 
(
	[id_tipoDocumento] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tipos_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tipos_items](
	[id_tipo] [int] IDENTITY(1,1) NOT NULL,
	[tipo] [nvarchar](50) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_tipos_items] PRIMARY KEY CLUSTERED 
(
	[id_tipo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tmpcobros_retenciones]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tmpcobros_retenciones](
	[id_tmpRetencion] [int] IDENTITY(1,1) NOT NULL,
	[id_impuesto] [int] NOT NULL,
	[total] [decimal](18, 3) NOT NULL,
	[notas] [nvarchar](max) NULL,
 CONSTRAINT [PK_tmpretenciones] PRIMARY KEY CLUSTERED 
(
	[id_tmpRetencion] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tmpOC_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tmpOC_items](
	[id_tmpOCItem] [int] IDENTITY(1,1) NOT NULL,
	[id_ocItem] [int] NULL,
	[id_ordenCompra] [int] NULL,
	[id_item] [int] NULL,
	[cantidad] [int] NOT NULL,
	[precio] [decimal](18, 3) NOT NULL,
	[activo] [bit] NULL,
	[descript] [nvarchar](100) NULL,
	[cantidad_recibida] [int] NULL,
	[id_usuario] [int] NOT NULL,
 CONSTRAINT [PK_tmpOC_items] PRIMARY KEY CLUSTERED 
(
	[id_tmpOCItem] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tmppedidos_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tmppedidos_items](
	[id_tmpPedidoItem] [int] IDENTITY(1,1) NOT NULL,
	[id_pedidoItem] [int] NULL,
	[id_pedido] [int] NULL,
	[id_item] [int] NULL,
	[cantidad] [int] NOT NULL,
	[precio] [decimal](18, 2) NOT NULL,
	[activo] [bit] NULL,
	[descript] [nvarchar](100) NULL,
	[id_usuario] [int] NOT NULL,
	[id_unico] [uniqueidentifier] NOT NULL,
 CONSTRAINT [PK_tmppedidos_items] PRIMARY KEY NONCLUSTERED 
(
	[id_tmpPedidoItem] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Index [IX_tmppedidos_items]    Script Date: 17/7/2025 14:18:31 ******/
CREATE CLUSTERED INDEX [IX_tmppedidos_items] ON [dbo].[tmppedidos_items]
(
	[id_item] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tmpproduccion_asocItems]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tmpproduccion_asocItems](
	[id_tmpProduccion_asocItem] [int] IDENTITY(1,1) NOT NULL,
	[id_tmpProduccionItem] [int] NOT NULL,
	[id_produccionItem] [int] NULL,
	[id_produccion] [int] NULL,
	[id_item] [int] NOT NULL,
	[id_item_asoc] [int] NOT NULL,
	[cantidad_item_asoc_enviada] [int] NOT NULL,
	[id_usuario] [int] NOT NULL,
 CONSTRAINT [PK_tmpproduccion_asocItems] PRIMARY KEY CLUSTERED 
(
	[id_tmpProduccion_asocItem] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tmpproduccion_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tmpproduccion_items](
	[id_tmpProduccionItem] [int] IDENTITY(1,1) NOT NULL,
	[id_produccionItem] [int] NULL,
	[id_produccion] [int] NULL,
	[id_item] [int] NULL,
	[cantidad] [int] NOT NULL,
	[activo] [bit] NULL,
	[descript] [nvarchar](100) NULL,
	[id_item_recibido] [int] NULL,
	[cantidad_recibida] [int] NULL,
	[id_usuario] [int] NOT NULL,
 CONSTRAINT [PK_tmpproduccion_items] PRIMARY KEY CLUSTERED 
(
	[id_tmpProduccionItem] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tmpregistros_stock]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tmpregistros_stock](
	[id_registrotmp] [int] IDENTITY(1,1) NOT NULL,
	[id_ingreso] [int] NOT NULL,
	[fecha] [date] NULL,
	[fecha_ingreso] [date] NOT NULL,
	[factura] [nvarchar](50) NULL,
	[archivofc] [image] NULL,
	[id_proveedor] [int] NOT NULL,
	[id_item] [int] NOT NULL,
	[cantidad] [int] NOT NULL,
	[costo] [decimal](18, 2) NOT NULL,
	[precio_lista] [decimal](18, 2) NOT NULL,
	[factor] [decimal](18, 2) NULL,
	[cantidad_anterior] [int] NOT NULL,
	[costo_anterior] [decimal](18, 2) NOT NULL,
	[precio_lista_anterior] [decimal](18, 2) NOT NULL,
	[factor_anterior] [decimal](18, 2) NOT NULL,
	[nota] [varchar](max) NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_tmpregistros_stock] PRIMARY KEY CLUSTERED 
(
	[id_registrotmp] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tmpSelCH]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tmpSelCH](
	[id_cobro] [int] NULL,
	[id_pago] [int] NULL,
	[id_cheque] [int] NOT NULL,
	[seleccionado] [bit] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tmptransferencias]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tmptransferencias](
	[id_tmpTransferencia] [int] IDENTITY(1,1) NOT NULL,
	[id_cuentaBancaria] [int] NOT NULL,
	[fecha] [date] NOT NULL,
	[total] [decimal](18, 3) NOT NULL,
	[nComprobante] [nvarchar](50) NULL,
	[notas] [nvarchar](max) NULL,
 CONSTRAINT [PK_tmptransferencias] PRIMARY KEY CLUSTERED 
(
	[id_tmpTransferencia] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[transacciones]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[transacciones](
	[id_transaccion] [int] IDENTITY(1,1) NOT NULL,
	[fecha] [date] NOT NULL,
	[id_pedido] [int] NULL,
	[id_comprobanteCompra] [int] NULL,
	[id_cobro] [int] NULL,
	[id_pago] [int] NULL,
	[id_tipoComprobante] [int] NULL,
	[numeroComprobante] [int] NULL,
	[puntoVenta] [int] NULL,
	[total] [decimal](18, 3) NULL,
	[id_cc] [int] NULL,
	[id_cliente] [int] NULL,
	[id_proveedor] [int] NULL,
 CONSTRAINT [PK_transacciones] PRIMARY KEY CLUSTERED 
(
	[id_transaccion] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[transferencias]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[transferencias](
	[id_transferencia] [int] IDENTITY(1,1) NOT NULL,
	[id_cobro] [int] NULL,
	[id_pago] [int] NULL,
	[id_cuentaBancaria] [int] NOT NULL,
	[fecha] [date] NOT NULL,
	[total] [decimal](18, 3) NOT NULL,
	[nComprobante] [nvarchar](50) NULL,
	[notas] [nvarchar](max) NULL,
 CONSTRAINT [PK_cobros_transferencias] PRIMARY KEY CLUSTERED 
(
	[id_transferencia] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[usuarios]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[usuarios](
	[id_usuario] [int] IDENTITY(1,1) NOT NULL,
	[usuario] [nvarchar](20) NOT NULL,
	[password] [nvarchar](50) NOT NULL,
	[nombre] [nvarchar](50) NOT NULL,
	[activo] [bit] NOT NULL,
	[logueado] [bit] NOT NULL,
 CONSTRAINT [PK_usuarios] PRIMARY KEY CLUSTERED 
(
	[id_usuario] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[usuarios_perfiles]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[usuarios_perfiles](
	[id_usuario] [int] NOT NULL,
	[id_perfil] [int] NOT NULL,
 CONSTRAINT [PK_usuarios_perfiles] PRIMARY KEY CLUSTERED 
(
	[id_usuario] ASC,
	[id_perfil] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [IX_marcas_items_1]    Script Date: 17/7/2025 14:18:31 ******/
CREATE UNIQUE NONCLUSTERED INDEX [IX_marcas_items_1] ON [dbo].[marcas_items]
(
	[marca] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [IX_tipos_items]    Script Date: 17/7/2025 14:18:31 ******/
CREATE UNIQUE NONCLUSTERED INDEX [IX_tipos_items] ON [dbo].[tipos_items]
(
	[tipo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[ajustes_stock] ADD  CONSTRAINT [DF_ajustes_stock_fecha]  DEFAULT (CONVERT([date],getdate())) FOR [fecha]
GO
ALTER TABLE [dbo].[cambios] ADD  CONSTRAINT [DF_cambios_fecha]  DEFAULT (getdate()) FOR [fecha]
GO
ALTER TABLE [dbo].[cambios] ADD  CONSTRAINT [DF_cambios_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[cc_clientes] ADD  CONSTRAINT [DF_cc_clientes_id_moneda]  DEFAULT ((1)) FOR [id_moneda]
GO
ALTER TABLE [dbo].[cc_clientes] ADD  CONSTRAINT [DF_cc_clientes_saldo]  DEFAULT ((0)) FOR [saldo]
GO
ALTER TABLE [dbo].[cc_clientes] ADD  CONSTRAINT [DF_cc_clientes_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[cc_proveedores] ADD  CONSTRAINT [DF_cc_proveedores_id_moneda]  DEFAULT ((1)) FOR [id_moneda]
GO
ALTER TABLE [dbo].[cc_proveedores] ADD  CONSTRAINT [DF_cc_proveedores_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[cheques] ADD  CONSTRAINT [DF_cheques_fecha_ingreso]  DEFAULT (CONVERT([date],getdate())) FOR [fecha_ingreso]
GO
ALTER TABLE [dbo].[cheques] ADD  CONSTRAINT [DF_cheques_id_cliente]  DEFAULT (NULL) FOR [id_cliente]
GO
ALTER TABLE [dbo].[cheques] ADD  CONSTRAINT [DF_cheques_id_proveedor]  DEFAULT (NULL) FOR [id_proveedor]
GO
ALTER TABLE [dbo].[cheques] ADD  CONSTRAINT [DF_cheques_id_estadoC]  DEFAULT ((1)) FOR [id_estadoch]
GO
ALTER TABLE [dbo].[cheques] ADD  CONSTRAINT [DF_cheques_fecha_cobro]  DEFAULT (NULL) FOR [fecha_cobro]
GO
ALTER TABLE [dbo].[cheques] ADD  CONSTRAINT [DF_cheques_fecha_salida]  DEFAULT (NULL) FOR [fecha_salida]
GO
ALTER TABLE [dbo].[cheques] ADD  CONSTRAINT [DF_cheques_fecha_deposito]  DEFAULT (NULL) FOR [fecha_deposito]
GO
ALTER TABLE [dbo].[cheques] ADD  CONSTRAINT [DF_cheques_id_cuentaBancaria]  DEFAULT (NULL) FOR [id_cuentaBancaria]
GO
ALTER TABLE [dbo].[cheques] ADD  CONSTRAINT [DF_cheques_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[clientes] ADD  CONSTRAINT [DF_clientes_esInscripto]  DEFAULT ((1)) FOR [esInscripto]
GO
ALTER TABLE [dbo].[clientes] ADD  CONSTRAINT [DF_clientes_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[cobros] ADD  CONSTRAINT [DF_cobros_id_cobro_no_oficial]  DEFAULT ((-1)) FOR [id_cobro_no_oficial]
GO
ALTER TABLE [dbo].[cobros] ADD  CONSTRAINT [DF_cobros_fecha_carga]  DEFAULT (CONVERT([date],getdate())) FOR [fecha_carga]
GO
ALTER TABLE [dbo].[cobros] ADD  CONSTRAINT [DF_cobros_dineroEnCc]  DEFAULT ((0)) FOR [dineroEnCc]
GO
ALTER TABLE [dbo].[cobros] ADD  CONSTRAINT [DF_cobros_efectivo]  DEFAULT ((0)) FOR [efectivo]
GO
ALTER TABLE [dbo].[cobros] ADD  CONSTRAINT [DF_cobros_transferencia]  DEFAULT ((0)) FOR [totalTransferencia]
GO
ALTER TABLE [dbo].[cobros] ADD  CONSTRAINT [DF_cobros_totalCh]  DEFAULT ((0)) FOR [totalCh]
GO
ALTER TABLE [dbo].[cobros] ADD  CONSTRAINT [DF_cobros_totalRetencion]  DEFAULT ((0)) FOR [totalRetencion]
GO
ALTER TABLE [dbo].[cobros] ADD  CONSTRAINT [DF_cobros_total]  DEFAULT ((0)) FOR [total]
GO
ALTER TABLE [dbo].[cobros] ADD  CONSTRAINT [DF_cobros_activo_1]  DEFAULT ((0)) FOR [activo]
GO
ALTER TABLE [dbo].[comprobantes] ADD  CONSTRAINT [DF_comprobantes_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[comprobantes] ADD  CONSTRAINT [DF_comprobantes_testing]  DEFAULT ((0)) FOR [testing]
GO
ALTER TABLE [dbo].[comprobantes_compras] ADD  CONSTRAINT [DF_comprobantes_compras_fecha_carga]  DEFAULT (CONVERT([date],getdate())) FOR [fecha_carga]
GO
ALTER TABLE [dbo].[comprobantes_compras] ADD  CONSTRAINT [DF_comprobantes_compras_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[consultas_personalizadas] ADD  CONSTRAINT [DF_consultas_personalizadas_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[cuentas_bancarias] ADD  CONSTRAINT [DF_cuentas_bancarias_saldo]  DEFAULT ((0)) FOR [saldo]
GO
ALTER TABLE [dbo].[impuestos] ADD  CONSTRAINT [DF_impuestos_esRetencion]  DEFAULT ((0)) FOR [esRetencion]
GO
ALTER TABLE [dbo].[impuestos] ADD  CONSTRAINT [DF_impuestos_esPercepcion]  DEFAULT ((0)) FOR [esPercepcion]
GO
ALTER TABLE [dbo].[impuestos] ADD  CONSTRAINT [DF_impuestos_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[items] ADD  CONSTRAINT [DF_items_cantidad]  DEFAULT ((0)) FOR [cantidad]
GO
ALTER TABLE [dbo].[items] ADD  CONSTRAINT [DF_items_activo]  DEFAULT ((0)) FOR [esDescuento]
GO
ALTER TABLE [dbo].[items] ADD  CONSTRAINT [DF_items_activo_1]  DEFAULT ((0)) FOR [esMarkup]
GO
ALTER TABLE [dbo].[items] ADD  CONSTRAINT [DF_items_activo_2]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[items_impuestos] ADD  CONSTRAINT [DF_items_impuestos_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[marcas_items] ADD  CONSTRAINT [DF_marcas_items_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[ordenes_compras] ADD  CONSTRAINT [DF_ordenes_compras_fecha]  DEFAULT (CONVERT([date],getdate())) FOR [fecha_carga]
GO
ALTER TABLE [dbo].[ordenes_compras] ADD  CONSTRAINT [DF_ordenes_compras_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[pagos] ADD  CONSTRAINT [DF_pagos_fecha_carga]  DEFAULT (CONVERT([date],getdate())) FOR [fecha_carga]
GO
ALTER TABLE [dbo].[pagos] ADD  CONSTRAINT [DF_pagos_dineroEnCc]  DEFAULT ((0)) FOR [dineroEnCc]
GO
ALTER TABLE [dbo].[pagos] ADD  CONSTRAINT [DF_pagos_efectivo]  DEFAULT ((0)) FOR [efectivo]
GO
ALTER TABLE [dbo].[pagos] ADD  CONSTRAINT [DF_pagos_transferencia]  DEFAULT ((0)) FOR [totalTransferencia]
GO
ALTER TABLE [dbo].[pagos] ADD  CONSTRAINT [DF_pagos_totalCh]  DEFAULT ((0)) FOR [totalCh]
GO
ALTER TABLE [dbo].[pagos] ADD  CONSTRAINT [DF_pagos_total]  DEFAULT ((0)) FOR [total]
GO
ALTER TABLE [dbo].[pagos] ADD  CONSTRAINT [DF_pagos_activo]  DEFAULT ((0)) FOR [activo]
GO
ALTER TABLE [dbo].[pedidos] ADD  CONSTRAINT [DF_pedidos_fecha_edicion]  DEFAULT (CONVERT([date],getdate())) FOR [fecha_edicion]
GO
ALTER TABLE [dbo].[pedidos] ADD  CONSTRAINT [DF_pedidos_esPresupuesto]  DEFAULT ((0)) FOR [esPresupuesto]
GO
ALTER TABLE [dbo].[pedidos] ADD  CONSTRAINT [DF_pedidos_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[pedidos] ADD  CONSTRAINT [DF_pedidos_cerrado]  DEFAULT ((0)) FOR [cerrado]
GO
ALTER TABLE [dbo].[pedidos] ADD  CONSTRAINT [DF_pedidos_esTest]  DEFAULT ((0)) FOR [esTest]
GO
ALTER TABLE [dbo].[pedidos] ADD  CONSTRAINT [DF_pedidos_esDuplicado]  DEFAULT ((0)) FOR [esDuplicado]
GO
ALTER TABLE [dbo].[pedidos_items] ADD  CONSTRAINT [DF_pedidos_items_precio]  DEFAULT ((1)) FOR [precio]
GO
ALTER TABLE [dbo].[pedidos_items] ADD  CONSTRAINT [DF_pedidos_items_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[produccion] ADD  CONSTRAINT [DF_produccion_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[produccion_items] ADD  CONSTRAINT [DF_produccion_items_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[proveedores] ADD  CONSTRAINT [DF_proveedores_esInscripto]  DEFAULT ((1)) FOR [esInscripto]
GO
ALTER TABLE [dbo].[proveedores] ADD  CONSTRAINT [DF_proveedores_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[registros_stock] ADD  CONSTRAINT [DF_registros_stock_fecha_ingreso]  DEFAULT (getdate()) FOR [fecha_ingreso]
GO
ALTER TABLE [dbo].[registros_stock] ADD  CONSTRAINT [DF_registros_stock_id_proveedor]  DEFAULT ((1)) FOR [id_proveedor]
GO
ALTER TABLE [dbo].[registros_stock] ADD  CONSTRAINT [DF_registros_stock_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[tipos_documentos] ADD  CONSTRAINT [DF_tipos_documentos_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[tipos_items] ADD  CONSTRAINT [DF_tipos_items_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[tmpOC_items] ADD  CONSTRAINT [DF_tmpOC_items_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[tmppedidos_items] ADD  CONSTRAINT [DF_tmppedidos_items_id_pedido]  DEFAULT (NULL) FOR [id_pedido]
GO
ALTER TABLE [dbo].[tmppedidos_items] ADD  CONSTRAINT [DF_tmppedidos_items_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[tmpproduccion_items] ADD  CONSTRAINT [DF_tmpproduccion_items_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[tmpregistros_stock] ADD  CONSTRAINT [DF_tmpregistros_stock_id_ingreso]  DEFAULT ([dbo].[idultimoingreso]()+(1)) FOR [id_ingreso]
GO
ALTER TABLE [dbo].[tmpregistros_stock] ADD  CONSTRAINT [DF_tmpregistros_stock_fecha_ingreso]  DEFAULT (getdate()) FOR [fecha_ingreso]
GO
ALTER TABLE [dbo].[tmpregistros_stock] ADD  CONSTRAINT [DF_tmpregistros_stock_id_proveedor]  DEFAULT ((1)) FOR [id_proveedor]
GO
ALTER TABLE [dbo].[tmpregistros_stock] ADD  CONSTRAINT [DF_tmpregistros_stock_activo]  DEFAULT ((1)) FOR [activo]
GO
ALTER TABLE [dbo].[tmpSelCH] ADD  CONSTRAINT [DF_tmpSelCH_seleccionado]  DEFAULT ((0)) FOR [seleccionado]
GO
ALTER TABLE [dbo].[usuarios] ADD  CONSTRAINT [DF_usuarios_logueado]  DEFAULT ((0)) FOR [logueado]
GO
ALTER TABLE [dbo].[ajustes_stock]  WITH CHECK ADD  CONSTRAINT [FK_ajustes_stock_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[ajustes_stock] CHECK CONSTRAINT [FK_ajustes_stock_items]
GO
ALTER TABLE [dbo].[asocItems]  WITH CHECK ADD  CONSTRAINT [FK_asocItems_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[asocItems] CHECK CONSTRAINT [FK_asocItems_items]
GO
ALTER TABLE [dbo].[asocItems]  WITH CHECK ADD  CONSTRAINT [FK_asocItems_items1] FOREIGN KEY([id_item_asoc])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[asocItems] CHECK CONSTRAINT [FK_asocItems_items1]
GO
ALTER TABLE [dbo].[bancos]  WITH CHECK ADD  CONSTRAINT [FK_bancos_paises] FOREIGN KEY([id_pais])
REFERENCES [dbo].[paises] ([id_pais])
GO
ALTER TABLE [dbo].[bancos] CHECK CONSTRAINT [FK_bancos_paises]
GO
ALTER TABLE [dbo].[cc_clientes]  WITH NOCHECK ADD  CONSTRAINT [FK_cc_clientes_clientes] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[clientes] ([id_cliente])
GO
ALTER TABLE [dbo].[cc_clientes] NOCHECK CONSTRAINT [FK_cc_clientes_clientes]
GO
ALTER TABLE [dbo].[cc_clientes]  WITH CHECK ADD  CONSTRAINT [FK_cc_clientes_sysMoneda] FOREIGN KEY([id_moneda])
REFERENCES [dbo].[sysMoneda] ([id_moneda])
GO
ALTER TABLE [dbo].[cc_clientes] CHECK CONSTRAINT [FK_cc_clientes_sysMoneda]
GO
ALTER TABLE [dbo].[cc_proveedores]  WITH CHECK ADD  CONSTRAINT [FK_cc_proveedores_proveedores] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[proveedores] ([id_proveedor])
GO
ALTER TABLE [dbo].[cc_proveedores] CHECK CONSTRAINT [FK_cc_proveedores_proveedores]
GO
ALTER TABLE [dbo].[cc_proveedores]  WITH CHECK ADD  CONSTRAINT [FK_cc_proveedores_sysMoneda] FOREIGN KEY([id_moneda])
REFERENCES [dbo].[sysMoneda] ([id_moneda])
GO
ALTER TABLE [dbo].[cc_proveedores] CHECK CONSTRAINT [FK_cc_proveedores_sysMoneda]
GO
ALTER TABLE [dbo].[cheques]  WITH CHECK ADD  CONSTRAINT [FK_cheques_bancos] FOREIGN KEY([id_banco])
REFERENCES [dbo].[bancos] ([id_banco])
GO
ALTER TABLE [dbo].[cheques] CHECK CONSTRAINT [FK_cheques_bancos]
GO
ALTER TABLE [dbo].[cheques]  WITH NOCHECK ADD  CONSTRAINT [FK_cheques_clientes] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[clientes] ([id_cliente])
GO
ALTER TABLE [dbo].[cheques] NOCHECK CONSTRAINT [FK_cheques_clientes]
GO
ALTER TABLE [dbo].[cheques]  WITH CHECK ADD  CONSTRAINT [FK_cheques_cuentas_bancarias] FOREIGN KEY([id_cuentaBancaria])
REFERENCES [dbo].[cuentas_bancarias] ([id_cuentaBancaria])
GO
ALTER TABLE [dbo].[cheques] CHECK CONSTRAINT [FK_cheques_cuentas_bancarias]
GO
ALTER TABLE [dbo].[cheques]  WITH CHECK ADD  CONSTRAINT [FK_cheques_proveedores] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[proveedores] ([id_proveedor])
GO
ALTER TABLE [dbo].[cheques] CHECK CONSTRAINT [FK_cheques_proveedores]
GO
ALTER TABLE [dbo].[cheques]  WITH CHECK ADD  CONSTRAINT [FK_cheques_sysestados_cheques] FOREIGN KEY([id_estadoch])
REFERENCES [dbo].[sysestados_cheques] ([id_estadoch])
GO
ALTER TABLE [dbo].[cheques] CHECK CONSTRAINT [FK_cheques_sysestados_cheques]
GO
ALTER TABLE [dbo].[clientes]  WITH NOCHECK ADD  CONSTRAINT [FK_clientes_provincias] FOREIGN KEY([id_provincia_fiscal])
REFERENCES [dbo].[provincias] ([id_provincia])
GO
ALTER TABLE [dbo].[clientes] NOCHECK CONSTRAINT [FK_clientes_provincias]
GO
ALTER TABLE [dbo].[clientes]  WITH NOCHECK ADD  CONSTRAINT [FK_clientes_provincias1] FOREIGN KEY([id_provincia_entrega])
REFERENCES [dbo].[provincias] ([id_provincia])
GO
ALTER TABLE [dbo].[clientes] NOCHECK CONSTRAINT [FK_clientes_provincias1]
GO
ALTER TABLE [dbo].[clientes]  WITH CHECK ADD  CONSTRAINT [FK_clientes_sys_ClasesFiscales] FOREIGN KEY([id_claseFiscal])
REFERENCES [dbo].[sys_ClasesFiscales] ([id_claseFiscal])
GO
ALTER TABLE [dbo].[clientes] CHECK CONSTRAINT [FK_clientes_sys_ClasesFiscales]
GO
ALTER TABLE [dbo].[clientes]  WITH NOCHECK ADD  CONSTRAINT [FK_clientes_tipos_documentos] FOREIGN KEY([id_tipoDocumento])
REFERENCES [dbo].[tipos_documentos] ([id_tipoDocumento])
GO
ALTER TABLE [dbo].[clientes] NOCHECK CONSTRAINT [FK_clientes_tipos_documentos]
GO
ALTER TABLE [dbo].[cobros]  WITH NOCHECK ADD  CONSTRAINT [FK_cobros_clientes] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[clientes] ([id_cliente])
GO
ALTER TABLE [dbo].[cobros] NOCHECK CONSTRAINT [FK_cobros_clientes]
GO
ALTER TABLE [dbo].[cobros_cheques]  WITH CHECK ADD  CONSTRAINT [FK_cobros_cheques_cheques] FOREIGN KEY([id_cheque])
REFERENCES [dbo].[cheques] ([id_cheque])
GO
ALTER TABLE [dbo].[cobros_cheques] CHECK CONSTRAINT [FK_cobros_cheques_cheques]
GO
ALTER TABLE [dbo].[cobros_cheques]  WITH CHECK ADD  CONSTRAINT [FK_cobros_cheques_cobros] FOREIGN KEY([id_cobro])
REFERENCES [dbo].[cobros] ([id_cobro])
GO
ALTER TABLE [dbo].[cobros_cheques] CHECK CONSTRAINT [FK_cobros_cheques_cobros]
GO
ALTER TABLE [dbo].[cobros_Nfacturas_importes]  WITH CHECK ADD  CONSTRAINT [FK_cobros_Nfacturas_importes_cobros] FOREIGN KEY([id_cobro])
REFERENCES [dbo].[cobros] ([id_cobro])
GO
ALTER TABLE [dbo].[cobros_Nfacturas_importes] CHECK CONSTRAINT [FK_cobros_Nfacturas_importes_cobros]
GO
ALTER TABLE [dbo].[cobros_retenciones]  WITH CHECK ADD  CONSTRAINT [FK_cobros_retenciones_cobros] FOREIGN KEY([id_cobro])
REFERENCES [dbo].[cobros] ([id_cobro])
GO
ALTER TABLE [dbo].[cobros_retenciones] CHECK CONSTRAINT [FK_cobros_retenciones_cobros]
GO
ALTER TABLE [dbo].[cobros_retenciones]  WITH CHECK ADD  CONSTRAINT [FK_cobros_retenciones_impuestos] FOREIGN KEY([id_impuesto])
REFERENCES [dbo].[impuestos] ([id_impuesto])
GO
ALTER TABLE [dbo].[cobros_retenciones] CHECK CONSTRAINT [FK_cobros_retenciones_impuestos]
GO
ALTER TABLE [dbo].[comprobantes]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_sys_modoMiPyme] FOREIGN KEY([id_modoMiPyme])
REFERENCES [dbo].[sys_modoMiPyme] ([id_modoMiPyme])
GO
ALTER TABLE [dbo].[comprobantes] CHECK CONSTRAINT [FK_comprobantes_sys_modoMiPyme]
GO
ALTER TABLE [dbo].[comprobantes]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_tipos_comprobantes] FOREIGN KEY([id_tipoComprobante])
REFERENCES [dbo].[tipos_comprobantes] ([id_tipoComprobante])
GO
ALTER TABLE [dbo].[comprobantes] CHECK CONSTRAINT [FK_comprobantes_tipos_comprobantes]
GO
ALTER TABLE [dbo].[comprobantes_compras]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_cc_proveedores] FOREIGN KEY([id_cc])
REFERENCES [dbo].[cc_proveedores] ([id_cc])
GO
ALTER TABLE [dbo].[comprobantes_compras] CHECK CONSTRAINT [FK_comprobantes_compras_cc_proveedores]
GO
ALTER TABLE [dbo].[comprobantes_compras]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_condiciones_compra] FOREIGN KEY([id_condicion_compra])
REFERENCES [dbo].[condiciones_compra] ([id_condicion_compra])
GO
ALTER TABLE [dbo].[comprobantes_compras] CHECK CONSTRAINT [FK_comprobantes_compras_condiciones_compra]
GO
ALTER TABLE [dbo].[comprobantes_compras]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_proveedores] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[proveedores] ([id_proveedor])
GO
ALTER TABLE [dbo].[comprobantes_compras] CHECK CONSTRAINT [FK_comprobantes_compras_proveedores]
GO
ALTER TABLE [dbo].[comprobantes_compras]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_sysMoneda] FOREIGN KEY([id_moneda])
REFERENCES [dbo].[sysMoneda] ([id_moneda])
GO
ALTER TABLE [dbo].[comprobantes_compras] CHECK CONSTRAINT [FK_comprobantes_compras_sysMoneda]
GO
ALTER TABLE [dbo].[comprobantes_compras]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_tipos_comprobantes] FOREIGN KEY([id_tipoComprobante])
REFERENCES [dbo].[tipos_comprobantes] ([id_tipoComprobante])
GO
ALTER TABLE [dbo].[comprobantes_compras] CHECK CONSTRAINT [FK_comprobantes_compras_tipos_comprobantes]
GO
ALTER TABLE [dbo].[comprobantes_compras_conceptos]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_conceptos_comprobantes_compras] FOREIGN KEY([id_comprobanteCompra])
REFERENCES [dbo].[comprobantes_compras] ([id_comprobanteCompra])
GO
ALTER TABLE [dbo].[comprobantes_compras_conceptos] CHECK CONSTRAINT [FK_comprobantes_compras_conceptos_comprobantes_compras]
GO
ALTER TABLE [dbo].[comprobantes_compras_conceptos]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_conceptos_conceptos_compra] FOREIGN KEY([id_concepto_compra])
REFERENCES [dbo].[conceptos_compra] ([id_concepto_compra])
GO
ALTER TABLE [dbo].[comprobantes_compras_conceptos] CHECK CONSTRAINT [FK_comprobantes_compras_conceptos_conceptos_compra]
GO
ALTER TABLE [dbo].[comprobantes_compras_impuestos]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_impuestos_comprobantes_compras] FOREIGN KEY([id_comprobanteCompra])
REFERENCES [dbo].[comprobantes_compras] ([id_comprobanteCompra])
GO
ALTER TABLE [dbo].[comprobantes_compras_impuestos] CHECK CONSTRAINT [FK_comprobantes_compras_impuestos_comprobantes_compras]
GO
ALTER TABLE [dbo].[comprobantes_compras_impuestos]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_impuestos_impuestos] FOREIGN KEY([id_impuesto])
REFERENCES [dbo].[impuestos] ([id_impuesto])
GO
ALTER TABLE [dbo].[comprobantes_compras_impuestos] CHECK CONSTRAINT [FK_comprobantes_compras_impuestos_impuestos]
GO
ALTER TABLE [dbo].[comprobantes_compras_items]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_items_comprobantes_compras] FOREIGN KEY([id_comprobanteCompra])
REFERENCES [dbo].[comprobantes_compras] ([id_comprobanteCompra])
GO
ALTER TABLE [dbo].[comprobantes_compras_items] CHECK CONSTRAINT [FK_comprobantes_compras_items_comprobantes_compras]
GO
ALTER TABLE [dbo].[comprobantes_compras_items]  WITH CHECK ADD  CONSTRAINT [FK_comprobantes_compras_items_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[comprobantes_compras_items] CHECK CONSTRAINT [FK_comprobantes_compras_items_items]
GO
ALTER TABLE [dbo].[cuentas_bancarias]  WITH CHECK ADD  CONSTRAINT [FK_cuentas_bancarias_bancos] FOREIGN KEY([id_banco])
REFERENCES [dbo].[bancos] ([id_banco])
GO
ALTER TABLE [dbo].[cuentas_bancarias] CHECK CONSTRAINT [FK_cuentas_bancarias_bancos]
GO
ALTER TABLE [dbo].[cuentas_bancarias]  WITH CHECK ADD  CONSTRAINT [FK_cuentas_bancarias_sysMoneda] FOREIGN KEY([id_moneda])
REFERENCES [dbo].[sysMoneda] ([id_moneda])
GO
ALTER TABLE [dbo].[cuentas_bancarias] CHECK CONSTRAINT [FK_cuentas_bancarias_sysMoneda]
GO
ALTER TABLE [dbo].[items]  WITH CHECK ADD  CONSTRAINT [FK_items_marcas_items] FOREIGN KEY([id_marca])
REFERENCES [dbo].[marcas_items] ([id_marca])
GO
ALTER TABLE [dbo].[items] CHECK CONSTRAINT [FK_items_marcas_items]
GO
ALTER TABLE [dbo].[items]  WITH CHECK ADD  CONSTRAINT [FK_items_proveedores] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[proveedores] ([id_proveedor])
GO
ALTER TABLE [dbo].[items] CHECK CONSTRAINT [FK_items_proveedores]
GO
ALTER TABLE [dbo].[items]  WITH CHECK ADD  CONSTRAINT [FK_items_tipos_items] FOREIGN KEY([id_tipo])
REFERENCES [dbo].[tipos_items] ([id_tipo])
GO
ALTER TABLE [dbo].[items] CHECK CONSTRAINT [FK_items_tipos_items]
GO
ALTER TABLE [dbo].[items_impuestos]  WITH CHECK ADD  CONSTRAINT [FK_items_impuestos_impuestos] FOREIGN KEY([id_impuesto])
REFERENCES [dbo].[impuestos] ([id_impuesto])
GO
ALTER TABLE [dbo].[items_impuestos] CHECK CONSTRAINT [FK_items_impuestos_impuestos]
GO
ALTER TABLE [dbo].[items_impuestos]  WITH CHECK ADD  CONSTRAINT [FK_items_impuestos_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[items_impuestos] CHECK CONSTRAINT [FK_items_impuestos_items]
GO
ALTER TABLE [dbo].[ordenes_compras]  WITH CHECK ADD  CONSTRAINT [FK_ordenes_compras_proveedores] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[proveedores] ([id_proveedor])
GO
ALTER TABLE [dbo].[ordenes_compras] CHECK CONSTRAINT [FK_ordenes_compras_proveedores]
GO
ALTER TABLE [dbo].[ordenesCompras_items]  WITH CHECK ADD  CONSTRAINT [FK_ordenesCompra_items_ordenes_compras] FOREIGN KEY([id_ordenCompra])
REFERENCES [dbo].[ordenes_compras] ([id_ordenCompra])
GO
ALTER TABLE [dbo].[ordenesCompras_items] CHECK CONSTRAINT [FK_ordenesCompra_items_ordenes_compras]
GO
ALTER TABLE [dbo].[ordenesCompras_items]  WITH CHECK ADD  CONSTRAINT [FK_ordenesCompras_items_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[ordenesCompras_items] CHECK CONSTRAINT [FK_ordenesCompras_items_items]
GO
ALTER TABLE [dbo].[pagos]  WITH CHECK ADD  CONSTRAINT [FK_pagos_cc_proveedores] FOREIGN KEY([id_cc])
REFERENCES [dbo].[cc_proveedores] ([id_cc])
GO
ALTER TABLE [dbo].[pagos] CHECK CONSTRAINT [FK_pagos_cc_proveedores]
GO
ALTER TABLE [dbo].[pagos]  WITH CHECK ADD  CONSTRAINT [FK_pagos_proveedores] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[proveedores] ([id_proveedor])
GO
ALTER TABLE [dbo].[pagos] CHECK CONSTRAINT [FK_pagos_proveedores]
GO
ALTER TABLE [dbo].[pagos_cheques]  WITH CHECK ADD  CONSTRAINT [FK_pagos_cheques_cheques] FOREIGN KEY([id_cheque])
REFERENCES [dbo].[cheques] ([id_cheque])
GO
ALTER TABLE [dbo].[pagos_cheques] CHECK CONSTRAINT [FK_pagos_cheques_cheques]
GO
ALTER TABLE [dbo].[pagos_cheques]  WITH CHECK ADD  CONSTRAINT [FK_pagos_cheques_pagos] FOREIGN KEY([id_pago])
REFERENCES [dbo].[pagos] ([id_pago])
GO
ALTER TABLE [dbo].[pagos_cheques] CHECK CONSTRAINT [FK_pagos_cheques_pagos]
GO
ALTER TABLE [dbo].[pagos_nFacturas_importes]  WITH CHECK ADD  CONSTRAINT [FK_pagos_nFacturas_importes_pagos] FOREIGN KEY([id_pago])
REFERENCES [dbo].[pagos] ([id_pago])
GO
ALTER TABLE [dbo].[pagos_nFacturas_importes] CHECK CONSTRAINT [FK_pagos_nFacturas_importes_pagos]
GO
ALTER TABLE [dbo].[pedidos]  WITH CHECK ADD  CONSTRAINT [FK_pedidos_cc_clientes] FOREIGN KEY([id_cc], [id_cliente])
REFERENCES [dbo].[cc_clientes] ([id_cc], [id_cliente])
GO
ALTER TABLE [dbo].[pedidos] CHECK CONSTRAINT [FK_pedidos_cc_clientes]
GO
ALTER TABLE [dbo].[pedidos]  WITH NOCHECK ADD  CONSTRAINT [FK_pedidos_clientes] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[clientes] ([id_cliente])
GO
ALTER TABLE [dbo].[pedidos] NOCHECK CONSTRAINT [FK_pedidos_clientes]
GO
ALTER TABLE [dbo].[pedidos]  WITH CHECK ADD  CONSTRAINT [FK_pedidos_comprobantes] FOREIGN KEY([id_comprobante])
REFERENCES [dbo].[comprobantes] ([id_comprobante])
GO
ALTER TABLE [dbo].[pedidos] CHECK CONSTRAINT [FK_pedidos_comprobantes]
GO
ALTER TABLE [dbo].[pedidos]  WITH CHECK ADD  CONSTRAINT [FK_pedidos_usuarios] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuarios] ([id_usuario])
GO
ALTER TABLE [dbo].[pedidos] CHECK CONSTRAINT [FK_pedidos_usuarios]
GO
ALTER TABLE [dbo].[pedidos_items]  WITH CHECK ADD  CONSTRAINT [FK_pedidos_items_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[pedidos_items] CHECK CONSTRAINT [FK_pedidos_items_items]
GO
ALTER TABLE [dbo].[pedidos_items]  WITH CHECK ADD  CONSTRAINT [FK_pedidos_items_pedidos1] FOREIGN KEY([id_pedido])
REFERENCES [dbo].[pedidos] ([id_pedido])
GO
ALTER TABLE [dbo].[pedidos_items] CHECK CONSTRAINT [FK_pedidos_items_pedidos1]
GO
ALTER TABLE [dbo].[permisos_perfiles]  WITH CHECK ADD  CONSTRAINT [FK_permisos_perfiles_perfiles] FOREIGN KEY([id_pefil])
REFERENCES [dbo].[perfiles] ([id_perfil])
GO
ALTER TABLE [dbo].[permisos_perfiles] CHECK CONSTRAINT [FK_permisos_perfiles_perfiles]
GO
ALTER TABLE [dbo].[permisos_perfiles]  WITH CHECK ADD  CONSTRAINT [FK_permisos_perfiles_permisos] FOREIGN KEY([id_permiso])
REFERENCES [dbo].[permisos] ([id_permiso])
GO
ALTER TABLE [dbo].[permisos_perfiles] CHECK CONSTRAINT [FK_permisos_perfiles_permisos]
GO
ALTER TABLE [dbo].[produccion]  WITH CHECK ADD  CONSTRAINT [FK_produccion_proveedores] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[proveedores] ([id_proveedor])
GO
ALTER TABLE [dbo].[produccion] CHECK CONSTRAINT [FK_produccion_proveedores]
GO
ALTER TABLE [dbo].[produccion]  WITH CHECK ADD  CONSTRAINT [FK_produccion_usuarios] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuarios] ([id_usuario])
GO
ALTER TABLE [dbo].[produccion] CHECK CONSTRAINT [FK_produccion_usuarios]
GO
ALTER TABLE [dbo].[produccion_asocItems]  WITH CHECK ADD  CONSTRAINT [FK_produccion_asocItems_asocItems] FOREIGN KEY([id_item], [id_item_asoc])
REFERENCES [dbo].[asocItems] ([id_item], [id_item_asoc])
GO
ALTER TABLE [dbo].[produccion_asocItems] CHECK CONSTRAINT [FK_produccion_asocItems_asocItems]
GO
ALTER TABLE [dbo].[produccion_asocItems]  WITH CHECK ADD  CONSTRAINT [FK_produccion_asocItems_produccion] FOREIGN KEY([id_produccion])
REFERENCES [dbo].[produccion] ([id_produccion])
GO
ALTER TABLE [dbo].[produccion_asocItems] CHECK CONSTRAINT [FK_produccion_asocItems_produccion]
GO
ALTER TABLE [dbo].[produccion_items]  WITH CHECK ADD  CONSTRAINT [FK_produccion_items_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[produccion_items] CHECK CONSTRAINT [FK_produccion_items_items]
GO
ALTER TABLE [dbo].[produccion_items]  WITH CHECK ADD  CONSTRAINT [FK_produccion_items_items1] FOREIGN KEY([id_item_recibido])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[produccion_items] CHECK CONSTRAINT [FK_produccion_items_items1]
GO
ALTER TABLE [dbo].[produccion_items]  WITH CHECK ADD  CONSTRAINT [FK_produccion_items_produccion] FOREIGN KEY([id_produccion])
REFERENCES [dbo].[produccion] ([id_produccion])
GO
ALTER TABLE [dbo].[produccion_items] CHECK CONSTRAINT [FK_produccion_items_produccion]
GO
ALTER TABLE [dbo].[proveedores]  WITH CHECK ADD  CONSTRAINT [FK_proveedores_sys_ClasesFiscales] FOREIGN KEY([id_claseFiscal])
REFERENCES [dbo].[sys_ClasesFiscales] ([id_claseFiscal])
GO
ALTER TABLE [dbo].[proveedores] CHECK CONSTRAINT [FK_proveedores_sys_ClasesFiscales]
GO
ALTER TABLE [dbo].[provincias]  WITH CHECK ADD  CONSTRAINT [FK_provincias_paises] FOREIGN KEY([id_pais])
REFERENCES [dbo].[paises] ([id_pais])
GO
ALTER TABLE [dbo].[provincias] CHECK CONSTRAINT [FK_provincias_paises]
GO
ALTER TABLE [dbo].[registros_stock]  WITH CHECK ADD  CONSTRAINT [FK_registros_stock_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[registros_stock] CHECK CONSTRAINT [FK_registros_stock_items]
GO
ALTER TABLE [dbo].[registros_stock]  WITH CHECK ADD  CONSTRAINT [FK_registros_stock_proveedores] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[proveedores] ([id_proveedor])
GO
ALTER TABLE [dbo].[registros_stock] CHECK CONSTRAINT [FK_registros_stock_proveedores]
GO
ALTER TABLE [dbo].[tipos_comprobantes]  WITH CHECK ADD  CONSTRAINT [FK_tipos_comprobantes_sys_claseComprobante] FOREIGN KEY([id_claseComprobante])
REFERENCES [dbo].[sys_claseComprobante] ([id_claseComprobante])
GO
ALTER TABLE [dbo].[tipos_comprobantes] CHECK CONSTRAINT [FK_tipos_comprobantes_sys_claseComprobante]
GO
ALTER TABLE [dbo].[tmpcobros_retenciones]  WITH CHECK ADD  CONSTRAINT [FK_tmpretenciones_impuestos] FOREIGN KEY([id_impuesto])
REFERENCES [dbo].[impuestos] ([id_impuesto])
GO
ALTER TABLE [dbo].[tmpcobros_retenciones] CHECK CONSTRAINT [FK_tmpretenciones_impuestos]
GO
ALTER TABLE [dbo].[tmpOC_items]  WITH CHECK ADD  CONSTRAINT [FK_tmpOC_items_ordenes_compras] FOREIGN KEY([id_ordenCompra])
REFERENCES [dbo].[ordenes_compras] ([id_ordenCompra])
GO
ALTER TABLE [dbo].[tmpOC_items] CHECK CONSTRAINT [FK_tmpOC_items_ordenes_compras]
GO
ALTER TABLE [dbo].[tmpOC_items]  WITH CHECK ADD  CONSTRAINT [FK_tmpOC_items_ordenesCompra_items] FOREIGN KEY([id_ocItem])
REFERENCES [dbo].[ordenesCompras_items] ([id_ocItem])
GO
ALTER TABLE [dbo].[tmpOC_items] CHECK CONSTRAINT [FK_tmpOC_items_ordenesCompra_items]
GO
ALTER TABLE [dbo].[tmpOC_items]  WITH CHECK ADD  CONSTRAINT [FK_tmpOC_items_usuarios] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuarios] ([id_usuario])
GO
ALTER TABLE [dbo].[tmpOC_items] CHECK CONSTRAINT [FK_tmpOC_items_usuarios]
GO
ALTER TABLE [dbo].[tmppedidos_items]  WITH CHECK ADD  CONSTRAINT [FK_tmppedidos_items_pedidos] FOREIGN KEY([id_pedido])
REFERENCES [dbo].[pedidos] ([id_pedido])
GO
ALTER TABLE [dbo].[tmppedidos_items] CHECK CONSTRAINT [FK_tmppedidos_items_pedidos]
GO
ALTER TABLE [dbo].[tmppedidos_items]  WITH CHECK ADD  CONSTRAINT [FK_tmppedidos_items_pedidos_items] FOREIGN KEY([id_pedidoItem])
REFERENCES [dbo].[pedidos_items] ([id_pedidoItem])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[tmppedidos_items] CHECK CONSTRAINT [FK_tmppedidos_items_pedidos_items]
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems]  WITH CHECK ADD  CONSTRAINT [FK_tmpproduccion_asocItems_asocItems] FOREIGN KEY([id_item], [id_item_asoc])
REFERENCES [dbo].[asocItems] ([id_item], [id_item_asoc])
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems] CHECK CONSTRAINT [FK_tmpproduccion_asocItems_asocItems]
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems]  WITH CHECK ADD  CONSTRAINT [FK_tmpproduccion_asocItems_produccion] FOREIGN KEY([id_produccion])
REFERENCES [dbo].[produccion] ([id_produccion])
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems] CHECK CONSTRAINT [FK_tmpproduccion_asocItems_produccion]
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems]  WITH CHECK ADD  CONSTRAINT [FK_tmpproduccion_asocItems_produccion_items] FOREIGN KEY([id_produccionItem])
REFERENCES [dbo].[produccion_items] ([id_produccionItem])
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems] CHECK CONSTRAINT [FK_tmpproduccion_asocItems_produccion_items]
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems]  WITH CHECK ADD  CONSTRAINT [FK_tmpproduccion_asocItems_tmpproduccion_items] FOREIGN KEY([id_tmpProduccionItem])
REFERENCES [dbo].[tmpproduccion_items] ([id_tmpProduccionItem])
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems] CHECK CONSTRAINT [FK_tmpproduccion_asocItems_tmpproduccion_items]
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems]  WITH CHECK ADD  CONSTRAINT [FK_tmpproduccion_asocItems_usuarios] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuarios] ([id_usuario])
GO
ALTER TABLE [dbo].[tmpproduccion_asocItems] CHECK CONSTRAINT [FK_tmpproduccion_asocItems_usuarios]
GO
ALTER TABLE [dbo].[tmpproduccion_items]  WITH CHECK ADD  CONSTRAINT [FK_tmpproduccion_items_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[tmpproduccion_items] CHECK CONSTRAINT [FK_tmpproduccion_items_items]
GO
ALTER TABLE [dbo].[tmpproduccion_items]  WITH CHECK ADD  CONSTRAINT [FK_tmpproduccion_items_produccion] FOREIGN KEY([id_produccion])
REFERENCES [dbo].[produccion] ([id_produccion])
GO
ALTER TABLE [dbo].[tmpproduccion_items] CHECK CONSTRAINT [FK_tmpproduccion_items_produccion]
GO
ALTER TABLE [dbo].[tmpproduccion_items]  WITH CHECK ADD  CONSTRAINT [FK_tmpproduccion_items_usuarios] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuarios] ([id_usuario])
GO
ALTER TABLE [dbo].[tmpproduccion_items] CHECK CONSTRAINT [FK_tmpproduccion_items_usuarios]
GO
ALTER TABLE [dbo].[tmpregistros_stock]  WITH CHECK ADD  CONSTRAINT [FK_tmpregistros_stock_items] FOREIGN KEY([id_item])
REFERENCES [dbo].[items] ([id_item])
GO
ALTER TABLE [dbo].[tmpregistros_stock] CHECK CONSTRAINT [FK_tmpregistros_stock_items]
GO
ALTER TABLE [dbo].[tmpregistros_stock]  WITH CHECK ADD  CONSTRAINT [FK_tmpregistros_stock_proveedores] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[proveedores] ([id_proveedor])
GO
ALTER TABLE [dbo].[tmpregistros_stock] CHECK CONSTRAINT [FK_tmpregistros_stock_proveedores]
GO
ALTER TABLE [dbo].[tmpSelCH]  WITH CHECK ADD  CONSTRAINT [FK_tmpSelCH_cheques] FOREIGN KEY([id_cheque])
REFERENCES [dbo].[cheques] ([id_cheque])
GO
ALTER TABLE [dbo].[tmpSelCH] CHECK CONSTRAINT [FK_tmpSelCH_cheques]
GO
ALTER TABLE [dbo].[tmpSelCH]  WITH CHECK ADD  CONSTRAINT [FK_tmpSelCH_cobros] FOREIGN KEY([id_cobro])
REFERENCES [dbo].[cobros] ([id_cobro])
GO
ALTER TABLE [dbo].[tmpSelCH] CHECK CONSTRAINT [FK_tmpSelCH_cobros]
GO
ALTER TABLE [dbo].[tmpSelCH]  WITH CHECK ADD  CONSTRAINT [FK_tmpSelCH_pagos] FOREIGN KEY([id_pago])
REFERENCES [dbo].[pagos] ([id_pago])
GO
ALTER TABLE [dbo].[tmpSelCH] CHECK CONSTRAINT [FK_tmpSelCH_pagos]
GO
ALTER TABLE [dbo].[tmptransferencias]  WITH CHECK ADD  CONSTRAINT [FK_tmptransferencias_cuentas_bancarias] FOREIGN KEY([id_cuentaBancaria])
REFERENCES [dbo].[cuentas_bancarias] ([id_cuentaBancaria])
GO
ALTER TABLE [dbo].[tmptransferencias] CHECK CONSTRAINT [FK_tmptransferencias_cuentas_bancarias]
GO
ALTER TABLE [dbo].[transacciones]  WITH CHECK ADD  CONSTRAINT [FK_transacciones_cobros] FOREIGN KEY([id_cobro])
REFERENCES [dbo].[cobros] ([id_cobro])
GO
ALTER TABLE [dbo].[transacciones] CHECK CONSTRAINT [FK_transacciones_cobros]
GO
ALTER TABLE [dbo].[transacciones]  WITH CHECK ADD  CONSTRAINT [FK_transacciones_comprobantes_compras] FOREIGN KEY([id_comprobanteCompra])
REFERENCES [dbo].[comprobantes_compras] ([id_comprobanteCompra])
GO
ALTER TABLE [dbo].[transacciones] CHECK CONSTRAINT [FK_transacciones_comprobantes_compras]
GO
ALTER TABLE [dbo].[transacciones]  WITH CHECK ADD  CONSTRAINT [FK_transacciones_pagos] FOREIGN KEY([id_pago])
REFERENCES [dbo].[pagos] ([id_pago])
GO
ALTER TABLE [dbo].[transacciones] CHECK CONSTRAINT [FK_transacciones_pagos]
GO
ALTER TABLE [dbo].[transacciones]  WITH CHECK ADD  CONSTRAINT [FK_transacciones_pedidos] FOREIGN KEY([id_pedido])
REFERENCES [dbo].[pedidos] ([id_pedido])
GO
ALTER TABLE [dbo].[transacciones] CHECK CONSTRAINT [FK_transacciones_pedidos]
GO
ALTER TABLE [dbo].[transacciones]  WITH CHECK ADD  CONSTRAINT [FK_transacciones_tipos_comprobantes] FOREIGN KEY([id_tipoComprobante])
REFERENCES [dbo].[tipos_comprobantes] ([id_tipoComprobante])
GO
ALTER TABLE [dbo].[transacciones] CHECK CONSTRAINT [FK_transacciones_tipos_comprobantes]
GO
ALTER TABLE [dbo].[transferencias]  WITH CHECK ADD  CONSTRAINT [FK_cobros_transferencias_cobros] FOREIGN KEY([id_cobro])
REFERENCES [dbo].[cobros] ([id_cobro])
GO
ALTER TABLE [dbo].[transferencias] CHECK CONSTRAINT [FK_cobros_transferencias_cobros]
GO
ALTER TABLE [dbo].[transferencias]  WITH CHECK ADD  CONSTRAINT [FK_cobros_transferencias_cuentas_bancarias] FOREIGN KEY([id_cuentaBancaria])
REFERENCES [dbo].[cuentas_bancarias] ([id_cuentaBancaria])
GO
ALTER TABLE [dbo].[transferencias] CHECK CONSTRAINT [FK_cobros_transferencias_cuentas_bancarias]
GO
ALTER TABLE [dbo].[transferencias]  WITH CHECK ADD  CONSTRAINT [FK_transferencias_pagos] FOREIGN KEY([id_pago])
REFERENCES [dbo].[pagos] ([id_pago])
GO
ALTER TABLE [dbo].[transferencias] CHECK CONSTRAINT [FK_transferencias_pagos]
GO
ALTER TABLE [dbo].[usuarios_perfiles]  WITH CHECK ADD  CONSTRAINT [FK_usuarios_perfiles_perfiles] FOREIGN KEY([id_perfil])
REFERENCES [dbo].[perfiles] ([id_perfil])
GO
ALTER TABLE [dbo].[usuarios_perfiles] CHECK CONSTRAINT [FK_usuarios_perfiles_perfiles]
GO
ALTER TABLE [dbo].[usuarios_perfiles]  WITH CHECK ADD  CONSTRAINT [FK_usuarios_perfiles_usuarios] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuarios] ([id_usuario])
GO
ALTER TABLE [dbo].[usuarios_perfiles] CHECK CONSTRAINT [FK_usuarios_perfiles_usuarios]
GO
/****** Object:  StoredProcedure [dbo].[datos_empresa]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[datos_empresa]		
AS
BEGIN
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT nombre, direccion, dbo.mascaraCUIT(cuit) AS 'cuit', ingresos_brutos, inicio_actividades, logo
	FROM empresa
END
GO
/****** Object:  StoredProcedure [dbo].[factura_cabecera]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[factura_cabecera]
	-- Add the parameters for the stored procedure here
	@idfc INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT CONVERT(NVARCHAR(20), fecha_edicion, 103) AS 'order_date'
		, c.razon_social AS 'cust_name', 
		dbo.mascaraCUIT(c.taxNumber) AS 'cust_taxNumber'
		, c.direccion_fiscal AS 'cust_address' 
		, (CASE WHEN c.esInscripto = '1'  THEN 'Responsable Inscripto' END) AS 'inscripto'
		, pro.provincia AS 'provincia', c.localidad_fiscal AS 'localidad'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.subTotal AS MONEY),1))) AS 'subtotal'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.iva AS MONEY),1))) AS 'iva'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.total AS MONEY),1))) AS 'total'
		, p.nota1 AS 'nota1'
		, p.nota2 AS 'nota2'
		--, CONCAT('Nº  ', REPLICATE('0', 4 - LEN(p.puntoVenta)), p.puntoVenta, '-', REPLICATE('0', 8 - LEN(p.numeroComprobante)), p.numeroComprobante) AS 'numeroFC',
		 , CASE WHEN p.esPresupuesto = 1 THEN 
				dbo.CalculoComprobante(tcmp.nombreAbreviado, p.puntoVenta, p.idPresupuesto)
		   ELSE
				dbo.CalculoComprobante(tcmp.nombreAbreviado, p.puntoVenta, p.numeroComprobante)
			END AS 'numeroFC'
		 , p.cae AS 'CAE', CONVERT(NVARCHAR(20), p.fechaVencimiento_cae,103) AS 'vencimiento_cae'
		 , p.numeroComprobante AS 'numeroComprobante' 
		 , ISNULL(p.idPresupuesto, 1) AS 'idpresupuesto'
		 , p.codigoDeBarras AS 'codigoDeBarras'
		 , p.fc_qr AS 'fc_qr'
	FROM pedidos AS p			
	INNER JOIN clientes AS c ON p.id_cliente = c.id_cliente	
	INNER JOIN comprobantes AS cmp ON p.id_comprobante = cmp.id_comprobante	
	INNER JOIN tipos_comprobantes AS tcmp ON cmp.id_tipoComprobante = tcmp.id_tipoComprobante		
	INNER JOIN provincias AS pro ON c.id_provincia_fiscal = pro.id_provincia	
	WHERE p.id_pedido = @idfc	
END
GO
/****** Object:  StoredProcedure [dbo].[factura_detalle]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[factura_detalle]
	-- Add the parameters for the stored procedure here
	@idfc INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT CASE WHEN pit.id_item IS NOT NULL THEN i.item END AS 'item_code', 
		CASE WHEN pit.id_item IS NULL THEN pit.descript ELSE i.descript END AS 'item_desc',		
		CASE WHEN (i.esDescuento = '0' AND i.esMarkup = '0') OR pit.id_item IS NULL THEN dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(pit.cantidad AS INT),1)) END AS 'item_qty', 
		CASE WHEN (i.esDescuento = '0' AND i.esMarkup = '0') OR pit.id_item IS NULL THEN CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(pit.precio AS MONEY),1))) END 'item_price', 
		CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(pit.cantidad * pit.precio AS MONEY),1))) AS 'item_subtotal'		 
	FROM pedidos_items AS pit
	LEFT JOIN items AS i ON pit.id_item = i.id_item
	WHERE pit.id_pedido = @idfc	
	ORDER BY i.esDescuento, i.esMarkup ASC
	--ORDER BY pit.id_pedidoItem ASC
END
GO
/****** Object:  StoredProcedure [dbo].[presupuesto_cabecera]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[presupuesto_cabecera]
	-- Add the parameters for the stored procedure here
	@idfc INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT CONVERT(VARCHAR(10), fecha_edicion, 103) AS 'order_date', c.razon_social AS 'cust_name', c.taxNumber AS 'cust_taxNumber', c.direccion_entrega AS 'cust_address', 
		(CASE WHEN c.esInscripto = '1'  THEN 'Responsable Inscripto' END) AS 'inscripto', pro.provincia AS 'provincia', c.localidad_entrega AS 'localidad',
		 CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.subTotal AS MONEY),1))) AS 'subtotal', 
		 CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.iva AS MONEY),1))) AS 'iva',
		 CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.total AS MONEY),1))) AS 'total',
		 p.nota1 AS 'nota1', p.nota2 AS 'nota2', p.idPresupuesto AS 'idpresupuesto'
	FROM pedidos AS p			
	INNER JOIN clientes AS c ON p.id_cliente = c.id_cliente
	INNER JOIN provincias AS pro ON c.id_provincia_fiscal = pro.id_provincia 	
	WHERE p.id_pedido = @idfc	
END
GO
/****** Object:  StoredProcedure [dbo].[produccion_cabecera]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[produccion_cabecera]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT pr.id_produccion AS 'id', 
			p.razon_social AS 'proveedor',
			p.direccion_fiscal AS 'direccion_fiscal', 
			p.localidad_fiscal AS 'localidad_fiscal', 
			prov.provincia AS 'provincia_fiscal',
			p.taxNumber AS 'taxNumber',
			CONVERT(NVARCHAR(20), pr.fecha_carga, 103) AS 'fecha_carga',
			CONVERT(NVARCHAR(20), pr.fecha_envio, 103) AS 'fecha_envio', 
			CONVERT(NVARCHAR(20), pr.fecha_recepcion, 103) AS 'fecha_recepcion',
			CASE WHEN pr.enviado = 1 THEN 'Si' ELSE 'No' END AS 'enviado',
			CASE WHEN pr.enviado = 1 THEN 'Si' ELSE 'No' END AS 'recibido',
			pr.notas AS 'notas', 
			CASE WHEN pr.activo = 1 THEN 'Si' ELSE 'No' END AS 'activo'		
		FROM produccion AS pr
		INNER JOIN proveedores AS p ON pr.id_proveedor = p.id_proveedor	
		INNER JOIN provincias AS prov ON p.id_provincia_fiscal = prov.id_provincia
		WHERE pr.id_produccion = @id
END
GO
/****** Object:  StoredProcedure [dbo].[produccion_detalle]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[produccion_detalle]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 
			pri.id_produccionItem AS 'id',
			pri.id_produccion AS 'id_produccion', 
			i.item AS 'item', 
			pri.descript AS 'descript', 
			pri.cantidad AS 'cantidad', 
			ISNULL(pri.cantidad_recibida, 0) AS 'cantidad_recibida', 
			CASE WHEN pri.activo = 1 THEN 'Si' ELSE 'No' END AS 'activo'
	FROM produccion_items AS pri
	INNER JOIN items AS i ON pri.id_item = i.id_item
	LEFT JOIN items AS ii ON pri.id_item_recibido = ii.id_item
	WHERE pri.id_produccion = @id
	ORDER BY pri.id_produccionItem ASC
END
GO
/****** Object:  StoredProcedure [dbo].[remito_cabecera]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[remito_cabecera]
	-- Add the parameters for the stored procedure here
	@idfc INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT CONVERT(NVARCHAR(20), fecha_edicion, 103) AS 'order_date', c.razon_social AS 'cust_name', 
	dbo.mascaraCUIT(c.taxNumber) AS 'cust_taxNumber', c.direccion_entrega AS 'cust_address', 
		(CASE WHEN c.esInscripto = '1'  THEN 'Responsable Inscripto' END) AS 'inscripto', pro.provincia AS 'provincia', c.localidad_entrega AS 'localidad',
		p.subtotal AS 'subtotal', p.iva AS 'iva', CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.total AS MONEY),1))) AS 'total', 
		p.nota1 AS 'nota1', p.nota2 AS 'nota2'
	FROM pedidos AS p			
	INNER JOIN clientes AS c ON p.id_cliente = c.id_cliente
	INNER JOIN provincias AS pro ON c.id_provincia_entrega = pro.id_provincia 
	WHERE p.id_pedido = @idfc	
END
GO
/****** Object:  StoredProcedure [dbo].[remito_detalle]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[remito_detalle]
	-- Add the parameters for the stored procedure here
	@idfc INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT CASE WHEN pit.id_item IS NOT NULL THEN i.item END AS 'item_code', 
	CASE WHEN i.esDescuento = '0' AND i.esMarkup = '0' AND pit.id_item IS NOT NULL THEN
		i.descript 
	ELSE
		pit.descript 		
	END AS 'item_desc',	
	CASE WHEN (i.esDescuento = '0' AND i.esMarkup = '0') OR pit.id_item IS NULL THEN 
		dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(pit.cantidad AS INT),1)) 		
	END AS 'item_qty'	
	FROM pedidos_items AS pit
	LEFT JOIN items AS i ON pit.id_item = i.id_item
	WHERE pit.id_pedido = @idfc
	ORDER BY i.esDescuento, i.esMarkup DESC
	--ORDER BY pit.id_pedidoItem ASC
END
GO
/****** Object:  StoredProcedure [dbo].[SP_cerrarComprobanteCompra]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_cerrarComprobanteCompra]
	-- Add the parameters for the stored procedure here
	@id_comprobanteCompra AS INTEGER,
	@subtotal AS DECIMAL(18,3),
	@impuestos AS DECIMAL(18,3),
	@conceptos AS DECIMAL(18,3),
	@total AS DECIMAL(18,3),
	@nota AS NVARCHAR(MAX)	
AS
BEGIN	
	SET NOCOUNT ON;	
	UPDATE comprobantes_compras 
		SET subtotal = @subtotal,
		impuestos = @impuestos,
		conceptos = @conceptos,
		total = @total,
		nota = @nota,
		activo = '0'
	WHERE id_comprobanteCompra = @id_comprobanteCompra	
END
GO
/****** Object:  StoredProcedure [dbo].[SP_cierre_diario]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_cierre_diario]
	-- Add the parameters for the stored procedure here
	@id_empresa AS INTEGER,
	@fecha AS NVARCHAR(100)
AS
BEGIN	
	SET NOCOUNT ON;

	SET DATEFORMAT dmy; UPDATE empresa
	SET fecha = @fecha
	WHERE id_empresa = @id_empresa	
END
GO
/****** Object:  StoredProcedure [dbo].[SP_cobro_cabecera]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_cobro_cabecera]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 
		CASE WHEN c.id_cobro_no_oficial = -1 THEN 
			dbo.CalculoComprobante('RC', '1', c.id_cobro_oficial) 
		ELSE 
			dbo.CalculoComprobante('RC', '1', c.id_cobro_no_oficial) 
		END AS 'id_cobro'
		, CONVERT(NVARCHAR(20), c.fecha_carga, 103) AS 'fecha_carga' 
		, CONVERT(NVARCHAR(20), c.fecha_cobro, 103) AS 'fecha_cobro', c.id_cliente, cli.razon_social
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(c.dineroEnCc AS MONEY),1))) AS 'dineroEnCc'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(c.efectivo AS MONEY),1))) AS 'efectivo'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(c.totalTransferencia AS MONEY),1))) AS 'totalTransferencia'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(c.totalCh AS MONEY),1))) AS 'totalCh'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(c.totalRetencion AS MONEY),1))) AS 'totalRetencion'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(c.total AS MONEY),1))) AS 'total'
		, c.hayCheque
		, c.hayTransferencia
		, c.hayRetencion
		, c.activo
		, c.id_anulaCobro
		, c.notas
		, c.firmante
		, dbo.CantidadConLetra(c.total) AS 'totalChar', 
		cli.direccion_fiscal
		, dbo.mascaraCUIT(cli.taxNumber) AS 'taxNumber'
		, (CASE WHEN cli.esInscripto = '1' THEN 'Responsable Inscripto' END) AS 'inscripto'		
	FROM cobros AS c
	INNER JOIN clientes AS cli ON c.id_cliente = cli.id_cliente	
	WHERE c.id_cobro = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_comprobanteCompra_cabecera]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_comprobanteCompra_cabecera]
	-- Add the parameters for the stored procedure here
	@id AS INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT CONVERT(NVARCHAR(20), cc.fecha_carga, 103) AS 'fecha_carga'
		, CONVERT(NVARCHAR(20), cc.fecha_comprobante, 103) AS 'fecha_comprobante'
		, CONCAT(tc.comprobante_AFIP, ' Nº  ', REPLICATE('0', 4 - LEN(cc.puntoVenta)), cc.puntoVenta, '-', REPLICATE('0', 8 - LEN(cc.numeroComprobante)), cc.numeroComprobante) AS 'comprobante'
		, cnc.condicion AS 'condicion_compra'
		, p.razon_social AS 'razon_social'
		, dbo.mascaraCUIT(p.taxNumber) AS 'supp_taxNumber'
		, p.direccion_fiscal AS 'supp_address'
		, (CASE WHEN p.esInscripto = '1'  THEN 'Responsable Inscripto' END) AS 'inscripto'
		, prov.provincia AS 'provincia'
		, p.localidad_fiscal AS 'localidad'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(cc.subTotal AS MONEY),1))) AS 'subtotal'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(cc.impuestos AS MONEY),1))) AS 'impuestos'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(cc.conceptos AS MONEY),1))) AS 'conceptos'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(cc.total AS MONEY),1))) AS 'total'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(cc.tasaCambio AS MONEY),1))) AS 'total'
		, cc.nota AS 'nota'
		, cc.cae AS 'cae'		
	FROM comprobantes_compras AS cc
	INNER JOIN tipos_comprobantes AS tc ON cc.id_tipoComprobante = tc.id_tipoComprobante
	INNER JOIN proveedores AS p ON cc.id_proveedor = p.id_proveedor
	INNER JOIN cc_proveedores AS ccp ON cc.id_cc = ccp.id_cc
	INNER JOIN sysMoneda AS sm ON cc.id_moneda = sm.id_moneda
	INNER JOIN provincias AS prov ON p.id_provincia_fiscal = prov.id_provincia
	INNER JOIN condiciones_compra AS cnc ON cc.id_condicion_compra = cnc.id_condicion_compra	
	WHERE cc.id_comprobanteCompra = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_comprobanteCompra_detalle_conceptos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_comprobanteCompra_detalle_conceptos]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT ccc.id_concepto_compra AS 'id'
			, cc.concepto AS 'concepto'
			, ccc.subtotal AS 'subtotal'
			, ccc.iva AS 'iva'
			, ccc.total AS 'total'
	FROM comprobantes_compras_conceptos AS ccc
	INNER JOIN conceptos_compra AS cc ON ccc.id_concepto_compra = cc.id_concepto_compra
	WHERE ccc.id_comprobanteCompra = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_comprobanteCompra_detalle_impuestos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_comprobanteCompra_detalle_impuestos]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT i.id_impuesto AS 'id'
			, i.nombre AS 'impuesto'
			, cci.importe AS 'importe'
	FROM comprobantes_compras_impuestos AS cci 
	INNER JOIN impuestos AS i ON cci.id_impuesto = i.id_impuesto
	WHERE cci.id_comprobanteCompra = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_comprobanteCompra_detalle_items]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_comprobanteCompra_detalle_items]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT i.id_item AS 'id'
		, i.item AS 'codigo'
		, i.descript AS 'descript'
		, cci.cantidad AS 'cantidad'
		, cci.precio AS 'precio'
	FROM comprobantes_compras_items AS cci 
	INNER JOIN items AS i ON cci.id_item = i.id_item
	WHERE cci.id_comprobanteCompra = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_consulta_CC_Cliente]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_consulta_CC_Cliente]
	-- Add the parameters for the stored procedure here	
	@id_cliente AS INTEGER
	, @id_cc AS INTEGER
	, @fecha_desde AS NVARCHAR(100)
	, @fecha_hasta AS NVARCHAR(100)	
AS
BEGIN	
	/*DECLARE @id_cliente INTEGER;  
	DECLARE @id_cc AS INTEGER;
	DECLARE @fecha_desde DATE;
	DECLARE @fecha_hasta DATE;

	SET @id_cliente = '2152';
	SET @id_cc = '150';
	SET @fecha_desde = '01/01/1753';   
	SET @fecha_hasta =  '12/31/9998';*/	

	WITH tbl AS (
		SELECT DISTINCT t.id_transaccion
		, t.id_cliente
		, t.numeroComprobante
		, t.puntoVenta
		, t.id_tipoComprobante
		, tc.nombreAbreviado 
		, t.fecha 
		, (CASE WHEN t.id_tipoComprobante IN (1, 6, 11, 51, 201, 206, 211, 1006, 2, 7, 12, 52, 202, 207, 212, 1007, 1002, 1003, 1004, 1005, 1010) THEN T.total ELSE 0 END) AS 'debito'
		, (CASE WHEN t.id_tipoComprobante IN (3, 8, 13, 53, 203, 208, 213, 1008, 4, 9, 15, 54, 1009) THEN T.total * -1 ELSE 0 END) AS 'credito'
		, (CASE WHEN t.id_tipoComprobante IN (1, 6, 11, 51, 201, 206, 211, 1006, 2, 7, 12, 52, 202, 207, 212, 1007, 1002, 1003, 1004, 1005, 1010) THEN T.total WHEN t.id_tipoComprobante IN (3, 8, 13, 53, 203, 208, 213, 1008, 4, 9, 15, 54, 1009) THEN T.TOTAL * -1 ELSE 0 END) AS 'total'
		, t.id_cc
		FROM transacciones As t   
		--INNER JOIN comprobantes AS cmp ON t.id_comprobante = cmp.id_comprobante   		
		INNER JOIN tipos_comprobantes AS tc ON t.id_tipoComprobante = tc.id_tipoComprobante
		INNER JOIN comprobantes AS c ON tc.id_tipoComprobante = c.id_tipoComprobante
		WHERE t.id_cliente = @id_cliente 
		AND t.id_cc = @id_cc 
		AND t.fecha BETWEEN @fecha_desde AND @fecha_hasta
		AND c.contabilizar = 1
		-- AND t.activo = 0 AND t.cerrado = 1 
		--AND t.esTest = 0 AND t.esPresupuesto = 0   
		--AND cmp.id_tipoComprobante IN (1, 2, 3, 4, 6, 7, 8, 9, 11 ,12, 13, 15, 51, 52, 53, 54, 200, 201)   
	) 
	SELECT tbl.id_transaccion AS 'ID'
		, tbl.fecha AS 'Fecha'
		, dbo.CalculoComprobante(tbl.nombreAbreviado, tbl.puntoVenta, tbl.numeroComprobante) AS 'Comprobante'
		, tbl.debito AS 'Débito'
		, tbl.credito AS 'Crédito'
		, SUM(tbl.TOTAL) OVER (PARTITION BY tbl.id_cliente, tbl.id_cc  ORDER BY tbl.id_transaccion ROWS UNBOUNDED PRECEDING ) AS 'Saldo'  
	FROM tbl INNER JOIN cc_clientes AS ccc ON tbl.id_cc = ccc.id_cc   
	WHERE tbl.id_cliente = @id_cliente 
	AND tbl.id_cc = @id_cc 
	AND tbl.fecha BETWEEN @fecha_desde AND @fecha_hasta 
	--AND tbl.activo = 0 AND tbl.cerrado = 1 AND tbl.esTest = 0 AND tbl.esPresupuesto = 0  
	--AND tbl.id_tipoComprobante IN (1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 15, 51, 52, 53, 54, 200, 201)  
	--ORDER BY tbl.numeroComprobante ASC
	ORDER BY tbl.id_transaccion ASC
END
GO
/****** Object:  StoredProcedure [dbo].[SP_consulta_CC_Proveedor]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_consulta_CC_Proveedor]
	-- Add the parameters for the stored procedure here	
	@id_proveedor AS INTEGER
	, @id_cc AS INTEGER
	, @fecha_desde AS NVARCHAR(100)
	, @fecha_hasta AS NVARCHAR(100)	
AS
BEGIN	
	/*DECLARE @id_proveedor INTEGER;
	DECLARE @id_cc AS INTEGER;
	DECLARE @fecha_desde DATE;
	DECLARE @fecha_hasta DATE;  

	SET @id_proveedor = '1039';
	SET @id_cc = '15';
	SET @fecha_desde = '01/01/1753';   
	SET @fecha_hasta =  '12/31/9998';*/

WITH tbl AS (
	SELECT DISTINCT t.id_transaccion
	, t.id_proveedor
	, t.numeroComprobante
	, t.puntoVenta
	, t.id_tipoComprobante
	, tc.nombreAbreviado
	, t.fecha 
	, (CASE WHEN t.id_tipoComprobante IN (1, 6, 11, 51, 201, 206, 211, 1006, 2, 7, 12, 52, 202, 207, 212, 1007, 1002, 1003, 1004, 1005, 1010) THEN T.total ELSE 0 END) AS 'debito'
	, (CASE WHEN t.id_tipoComprobante IN (3, 8, 13, 53, 203, 208, 213, 1008, 4, 9, 15, 54, 1009) THEN T.total * -1 ELSE 0 END) AS 'credito'
	, (CASE WHEN t.id_tipoComprobante IN (1, 6, 11, 51, 201, 206, 211, 1006, 2, 7, 12, 52, 202, 207, 212, 1007, 1002, 1003, 1004, 1005, 1010) THEN T.total WHEN t.id_tipoComprobante IN (3, 8, 13, 53, 203, 208, 213, 1008, 4, 9, 15, 54, 1009) THEN T.TOTAL * -1 ELSE 0 END) AS 'total'
	, t.id_cc
	FROM transacciones As t   
	--INNER JOIN comprobantes AS cmp ON t.id_comprobante = cmp.id_comprobante   
	INNER JOIN tipos_comprobantes AS tc ON t.id_tipoComprobante = tc.id_tipoComprobante
	WHERE t.id_proveedor = @id_proveedor 
	AND t.id_cc = @id_cc 
	AND t.fecha BETWEEN @fecha_desde AND @fecha_hasta
	AND tc.contabilizar = 1
	-- AND t.activo = 0 AND t.cerrado = 1 
	--AND t.esTest = 0 AND t.esPresupuesto = 0   
	--AND cmp.id_tipoComprobante IN (1, 2, 3, 4, 6, 7, 8, 9, 11 ,12, 13, 15, 51, 52, 53, 54, 200, 201)   
) 
SELECT tbl.id_transaccion AS 'ID'
	, tbl.fecha AS 'Fecha'
	, dbo.CalculoComprobante(tbl.nombreAbreviado, tbl.puntoVenta, tbl.numeroComprobante) AS 'Comprobante' 
	, tbl.debito AS 'Débito'
	, tbl.credito AS 'Crédito'
	, SUM(tbl.TOTAL) OVER (PARTITION BY tbl.id_proveedor, tbl.id_cc ORDER BY tbl.id_transaccion ROWS UNBOUNDED PRECEDING ) AS 'Saldo'  
FROM tbl INNER JOIN cc_clientes AS ccc ON tbl.id_cc = ccc.id_cc   
WHERE tbl.id_proveedor = @id_proveedor AND tbl.id_cc = @id_cc AND tbl.fecha BETWEEN @fecha_desde AND @fecha_hasta 
--AND tbl.activo = 0 AND tbl.cerrado = 1 AND tbl.esTest = 0 AND tbl.esPresupuesto = 0  
--AND tbl.id_tipoComprobante IN (1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 15, 51, 52, 53, 54, 200, 201)  
--ORDER BY tbl.numeroComprobante ASC
ORDER BY tbl.id_transaccion ASC
END
GO
/****** Object:  StoredProcedure [dbo].[SP_detalle_cobros_cheques]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_detalle_cobros_cheques]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT ch.id_cheque
		, CONVERT(NVARCHAR(20)
		, ch.fecha_cobro, 103) AS 'fecha_ingreso'
		, b.nombre AS 'banco'
		--, cb.nombre AS 'cuenta_bancaria'
		, ch.nCheque
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(ch.importe AS MONEY),1))) AS 'importe'
	FROM cobros AS c
	INNER JOIN cobros_cheques AS cc ON c.id_cobro = cc.id_cobro
	INNER JOIN cheques AS ch ON cc.id_cheque = ch.id_cheque
	INNER JOIN bancos AS b ON ch.id_banco = b.id_banco
	--INNER JOIN cuentas_bancarias AS cb ON ch.id_cuentaBancaria = cb.id_cuentaBancaria
	WHERE c.id_cobro = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_detalle_cobros_fc_importes]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_detalle_cobros_fc_importes]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 
		id_cobro
		, CONVERT(NVARCHAR(20), fecha, 103) AS 'fecha'
		, nfactura		
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(importe AS MONEY),1))) AS 'importe'
	FROM cobros_Nfacturas_importes 	
	WHERE id_cobro = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_detalle_cobros_retenciones]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_detalle_cobros_retenciones]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT cr.id_retencion, i.nombre AS 'retencion', 
	CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(cr.total AS MONEY),1))) AS 'total', cr.notas
	FROM cobros AS c
	INNER JOIN cobros_retenciones AS cr ON c.id_cobro = cr.id_cobro		
	INNER JOIN impuestos AS i ON cr.id_impuesto = i.id_impuesto
	WHERE c.id_cobro = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_detalle_cobros_transferencias]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_detalle_cobros_transferencias]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT t.id_transferencia, CONVERT(NVARCHAR(20), t.fecha, 103) AS 'fecha', b.nombre AS 'banco', cb.nombre AS 'cuenta_bancaria',
	CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(t.total AS MONEY),1))) AS 'total', t.nComprobante, t.notas
	FROM cobros AS c
	INNER JOIN transferencias AS t ON c.id_cobro = t.id_cobro	
	INNER JOIN cuentas_bancarias AS cb ON t.id_cuentaBancaria = cb.id_cuentaBancaria
	INNER JOIN bancos AS b ON cb.id_banco = b.id_banco	
	WHERE c.id_cobro = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_detalle_pagos_cheques]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_detalle_pagos_cheques]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT ch.id_cheque
		, CONVERT(NVARCHAR(20), ch.fecha_cobro, 103) AS 'fecha_ingreso'
		, b.nombre AS 'banco'
		, ch.nCheque
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(ch.importe AS MONEY),1))) AS 'importe'
	FROM pagos AS p
	INNER JOIN pagos_cheques AS pc ON p.id_pago = pc.id_pago
	INNER JOIN cheques AS ch ON pc.id_cheque = ch.id_cheque
	INNER JOIN bancos AS b ON ch.id_banco = b.id_banco	
	WHERE p.id_pago = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_detalle_pagos_fc_importes]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_detalle_pagos_fc_importes]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 
		id_pago
		, CONVERT(NVARCHAR(20), fecha, 103) AS 'fecha'
		, nfactura		
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(importe AS MONEY),1))) AS 'importe'
	FROM pagos_Nfacturas_importes 	
	WHERE id_pago = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_detalle_pagos_transferencias]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[SP_detalle_pagos_transferencias]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT t.id_transferencia, CONVERT(NVARCHAR(20), t.fecha, 103) AS 'fecha', b.nombre AS 'banco', cb.nombre AS 'cuenta_bancaria',
	CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(t.total AS MONEY),1))) AS 'total', t.nComprobante, t.notas
	FROM pagos AS p
	INNER JOIN transferencias AS t ON p.id_pago = t.id_pago
	INNER JOIN cuentas_bancarias AS cb ON t.id_cuentaBancaria = cb.id_cuentaBancaria
	INNER JOIN bancos AS b ON cb.id_banco = b.id_banco	
	WHERE p.id_pago = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertAsocItemsProduccionTMP]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[SP_insertAsocItemsProduccionTMP]
	-- Add the parameters for the stored procedure here	
	@id_tmpProduccion_asocItem AS INTEGER
	, @id_tmpProduccionItem AS INTEGER
	, @id_item AS INTEGER
	, @id_item_asoc AS INTEGER
	, @cantidad_item_asoc_enviada AS INTEGER
	, @id_usuario AS INTEGER
	, @resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;

	INSERT INTO tmpproduccion_asocItems (
		id_tmpProduccionItem
		, id_item
		, id_item_asoc
		, cantidad_item_asoc_enviada
		, id_usuario
	)
	VALUES (
		@id_tmpProduccionItem
		, @id_item
		, @id_item_asoc
		, @cantidad_item_asoc_enviada
		, @id_usuario
	)

	SET @resultado = SCOPE_IDENTITY()	

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertCobro]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_insertCobro]
	-- Add the parameters for the stored procedure here
	@id_cobro_oficial AS INTEGER
	, @id_cobro_no_oficial AS INTEGER
	, @fecha_cobro AS NVARCHAR(100)
	, @id_cliente AS INTEGER
	, @id_cc AS INTEGER
	, @dineroEnCc AS DECIMAL(18,3)
	, @efectivo AS DECIMAL(18,3)
	, @totalTransferencia AS DECIMAL(18,3)
	, @totalCh AS DECIMAL(18,3)
	, @totalRetencion AS DECIMAL(18,3)
	, @total AS DECIMAL(18,3)
	, @hayCheque AS BIT
	, @hayTransferencia AS BIT
	, @hayRetencion AS BIT
	--, @aplicaFc AS NVARCHAR(MAX)
	, @id_anulaCobro AS INTEGER
	, @notas AS NVARCHAR(MAX)
	, @firmante AS NVARCHAR(50)	
	, @resultado AS INTEGER OUTPUT	
AS
BEGIN		
	DECLARE @resultado_transaccion AS INTEGER
	DECLARE @id_tipoComprobante AS INTEGER
	DECLARE @id_cobro AS INTEGER
	SET NOCOUNT ON;
	SET DATEFORMAT dmy;
	INSERT INTO cobros (
		id_cobro_oficial
		, id_cobro_no_oficial
		, fecha_cobro
		, id_cliente 
		, id_cc
		, dineroEnCc
		, efectivo
		, totalTransferencia
		, totalCh
		, totalRetencion
		, total
		, hayCheque
		, hayTransferencia
		, hayRetencion
		--, aplicaFc
		, id_anulaCobro
		, notas
		, firmante	
	)
	VALUES (
		@id_cobro_oficial
		, @id_cobro_no_oficial
		, @fecha_cobro
		, @id_cliente
		, @id_cc
		, @dineroEnCc
		, @efectivo
		, @totalTransferencia
		, @totalCh
		, @totalRetencion
		, @total
		, @hayCheque
		, @hayTransferencia
		, @hayRetencion
		--, @aplicaFc
		, @id_anulaCobro
		, @notas
		, @firmante
	)
	
	SELECT @resultado = SCOPE_IDENTITY()
					
	IF @resultado IS NULL
		SET @resultado = -1

	IF @resultado = -1
		RETURN @resultado

	SELECT @id_cobro = CASE WHEN id_cobro_no_oficial = -1 THEN id_cobro_oficial ELSE id_cobro_no_oficial END FROM cobros WHERE id_cobro = SCOPE_IDENTITY()

	SELECT @id_tipoComprobante = CASE WHEN total > 0 THEN 4 ELSE 1015 END 
	FROM cobros
	WHERE id_cobro = @resultado

	INSERT INTO transacciones (
		fecha
		, id_cobro
		, id_tipoComprobante
		, numeroComprobante
		, puntoVenta
		, total
		, id_cc
		, id_cliente
	)
	VALUES (
		@fecha_cobro
		, @resultado
		--, '4' --4 = RECIBO 
		, @id_tipoComprobante
		, @id_cobro
		, '1'
		, @total
		, @id_cc
		, @id_cliente
	)
	
	SET @resultado_transaccion = SCOPE_IDENTITY()

	IF @resultado_transaccion IS NULL
		DELETE cobros WHERE id_cobro = @resultado
	
	IF @resultado_transaccion IS NULL 
		SET @resultado = -1
	
	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertComprobanteCompra]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_insertComprobanteCompra]
	-- Add the parameters for the stored procedure here
	@fecha_comprobante AS NVARCHAR(100),
	@id_proveedor AS INTEGER,
	@id_cc AS DECIMAL(18,3),
	@id_condicion_compra AS INTEGER,
	@id_tipoComprobante AS INTEGER,
	@id_moneda AS DECIMAL(18,3),
	@tasaCambio AS DECIMAL(18,3),
	@puntoVenta AS INTEGER,
	@numeroComprobante AS INTEGER,
	@cae AS NVARCHAR(50), 
	@resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;
	SET DATEFORMAT dmy;
	INSERT INTO comprobantes_compras (
		fecha_comprobante,
		id_tipoComprobante, 
		id_proveedor,
		id_cc, 
		id_moneda,		
		puntoVenta, 
		numeroComprobante,
		id_condicion_compra, 
		tasaCambio,
		cae
	)
	VALUES (
		@fecha_comprobante,
		@id_tipoComprobante, 
		@id_proveedor,
		@id_cc, 
		@id_moneda,		
		@puntoVenta, 
		@numeroComprobante,
		@id_condicion_compra, 
		@tasaCambio,
		@cae
	)

	SET @resultado = SCOPE_IDENTITY()	

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertImpuesto]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_insertImpuesto]
	-- Add the parameters for the stored procedure here	
	@nombre AS NVARCHAR(100),
	@porcentaje AS DECIMAL(18,4),
	@esRetencion AS BIT, 
	@esPercepcion AS BIT,
	@activo AS BIT,	
	@resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;

	INSERT INTO impuestos (
		nombre,
		porcentaje,
		esRetencion,
		esPercepcion,
		activo
	)
	VALUES (
		@nombre,
		@porcentaje,
		@esRetencion,
		@esPercepcion,
		@activo
	)

	SET @resultado = SCOPE_IDENTITY()	

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertItemsOCTMP]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_insertItemsOCTMP]
	-- Add the parameters for the stored procedure here	
	@id_tmpOCItem AS INTEGER,
	@id_item AS INTEGER,
	@cantidad AS INTEGER,	
	@precio AS DECIMAL(18,3),
	@descript AS NVARCHAR(100),
	@resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;

	INSERT INTO tmpOC_items (		
		id_item,
		cantidad,
		precio,
		descript
	)
	VALUES (		
		@id_item,
		@cantidad,
		@precio,
		@descript
	)

	SET @resultado = SCOPE_IDENTITY()	

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertItemsProduccionTMP]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_insertItemsProduccionTMP]
	-- Add the parameters for the stored procedure here	
	@id_tmpProduccionItem AS INTEGER
	, @id_item AS INTEGER
	, @cantidad AS INTEGER
	, @descript AS NVARCHAR(100)
	, @id_usuario AS INTEGER
	, @resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;

	INSERT INTO tmpproduccion_items (		
		id_item
		, cantidad
		, descript
		, id_usuario
	)
	VALUES (		
		@id_item
		, @cantidad
		, @descript
		, @id_usuario
	)

	SET @resultado = SCOPE_IDENTITY()	

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertItemsTMP]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_insertItemsTMP]
	-- Add the parameters for the stored procedure here
	@id_tmpPedidoItem AS INTEGER
	, @id_item AS INTEGER
	, @cantidad AS INTEGER
	, @precio AS DECIMAL(18,2)
	, @descript AS NVARCHAR(100)
	, @item AS NVARCHAR(50)
	, @id_usuario AS INTEGER
	, @id_unico AS NVARCHAR(MAX)
	, @resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;

	IF @item = 'MANUAL'
		BEGIN
			INSERT tmppedidos_items (descript, cantidad, precio, id_usuario, id_unico) SELECT @descript, @cantidad, @precio, @id_usuario, @id_unico
		END
	ELSE
		BEGIN
			INSERT tmppedidos_items (id_item, cantidad, precio, id_usuario, id_unico) SELECT @id_item, @cantidad, @precio, @id_usuario, @id_unico
	END
	
	
	SET @resultado = 1
	RETURN
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertPago]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_insertPago]
	-- Add the parameters for the stored procedure here	
	@fecha_pago AS NVARCHAR(100)
	, @id_proveedor AS INTEGER
	, @id_cc AS INTEGER
	, @dineroEnCc AS DECIMAL(18,3)
	, @efectivo AS DECIMAL(18,3)
	, @totalTransferencia AS DECIMAL(18,3)
	, @totalCh AS DECIMAL(18,3)
	, @total AS DECIMAL(18,3)
	, @hayCheque AS BIT
	, @hayTransferencia AS BIT
	--, @esAnulacion AS BIT
	, @id_anulaPago AS BIT
	, @notas AS NVARCHAR(MAX)
		--, @aplicaFC AS NVARCHAR(MAX)
	, @resultado AS INTEGER OUTPUT
AS
BEGIN	
	DECLARE @resultado_transaccion AS INTEGER
	DECLARE @id_tipoComprobante AS INTEGER
	SET NOCOUNT ON;
	SET DATEFORMAT dmy;
	INSERT INTO pagos(
		fecha_pago
		, id_proveedor
		, id_cc
		, dineroEnCc
		, efectivo
		, totalTransferencia
		, totalCh
		, total
		, hayCheque
		, hayTransferencia
		--, esAnulacion
		, id_anulaPago
		, notas		
		--, aplicaFC
	)
	VALUES (		
		@fecha_pago
		, @id_proveedor
		, @id_cc
		, @dineroEnCc
		, @efectivo
		, @totalTransferencia
		, @totalCh
		, @total
		, @hayCheque
		, @hayTransferencia
		--, @esAnulacion
		, @id_anulaPago
		, @notas
		--, @aplicaFC
	)

	SET @resultado = SCOPE_IDENTITY()	

	IF @resultado IS NULL
		SET @resultado = -1
	
	IF @resultado = -1
		RETURN @resultado

	SELECT @id_tipoComprobante = CASE WHEN total > 0 THEN 4 ELSE 1015 END 
	FROM pagos
	WHERE id_pago = @resultado

	INSERT INTO transacciones (
		fecha
		, id_pago
		, id_tipoComprobante
		, numeroComprobante
		, puntoVenta
		, total
		, id_cc
		, id_proveedor
	)
	VALUES (
		@fecha_pago
		, @resultado
		--, '4' --4 = RECIBO
		, @id_tipoComprobante
		, @resultado
		, '1'
		, @total
		, @id_cc
		, @id_proveedor
	)
	
	SET @resultado_transaccion = SCOPE_IDENTITY()

	IF @resultado_transaccion IS NULL
		DELETE cobros WHERE id_cobro = @resultado
	
	IF @resultado_transaccion IS NULL 
		SET @resultado = -1

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertTmpCobroRetencion]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_insertTmpCobroRetencion]
	-- Add the parameters for the stored procedure here	
	@id_impuesto AS INTEGER,	
	@total AS DECIMAL(18,3),	
	@notas AS NVARCHAR(MAX),	
	@resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;

	INSERT INTO tmpcobros_retenciones (
		id_impuesto,
		total,
		notas
	)
	VALUES (
		@id_impuesto,
		@total,
		@notas
	)

	SET @resultado = SCOPE_IDENTITY()	

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_insertTmpTransferencia]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[SP_insertTmpTransferencia]
	-- Add the parameters for the stored procedure here	
	@id_cuentaBancaria AS INTEGER,
	@fecha AS NVARCHAR(100),	
	@total AS DECIMAL(18,3),
	@nComprobante AS NVARCHAR(100),
	@notas AS NVARCHAR(100),
	@resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;
	SET DATEFORMAT dmy;
	INSERT INTO tmptransferencias (		
		id_cuentaBancaria,
		fecha,
		total,
		nComprobante,
		notas
	)
	VALUES (		
		@id_cuentaBancaria,
		@fecha,
		@total,
		@nComprobante,
		@notas
	)

	SET @resultado = SCOPE_IDENTITY()	

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_pago_cabecera]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_pago_cabecera]
	-- Add the parameters for the stored procedure here
	@id INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 
		 dbo.CalculoComprobante('OP', '1', p.id_pago) AS 'nRecibo'
		, CONVERT(NVARCHAR(20), p.fecha_carga, 103) AS 'fecha_carga'
		, CONVERT(NVARCHAR(20), p.fecha_pago, 103) AS 'fecha_pago'
		, p.id_proveedor
		, pr.razon_social
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.dineroEnCc AS MONEY),1))) AS 'dineroEnCc'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.efectivo AS MONEY),1))) AS 'efectivo'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.totalTransferencia AS MONEY),1))) AS 'totalTransferencia'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.totalCh AS MONEY),1))) AS 'totalCh'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.total AS MONEY),1))) AS 'total'	
		, p.hayCheque
		, p.hayTransferencia
		, p.activo
		--, p.esAnulacion
		, p.id_anulaPago
		, p.notas
		--, p.aplicaFC
		, dbo.CantidadConLetra(p.total) AS 'totalChar' 
		, pr.direccion_fiscal, dbo.mascaraCUIT(pr.taxNumber) AS 'taxNumber'
		, (CASE WHEN pr.esInscripto = '1'  THEN 'Responsable Inscripto' END) AS 'inscripto'		
	FROM pagos AS p
	INNER JOIN proveedores AS pr ON p.id_proveedor = pr.id_proveedor
	WHERE p.id_pago = @id
END
GO
/****** Object:  StoredProcedure [dbo].[SP_proforma_cabecera]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_proforma_cabecera]
	-- Add the parameters for the stored procedure here
	@idfc INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT CONVERT(NVARCHAR(20), fecha_edicion, 103) AS 'order_date'
		, c.razon_social AS 'cust_name', 
		dbo.mascaraCUIT(c.taxNumber) AS 'cust_taxNumber'
		, c.direccion_fiscal AS 'cust_address' 
		, (CASE WHEN c.esInscripto = '1'  THEN 'Responsable Inscripto' END) AS 'inscripto'
		, pro.provincia AS 'provincia', c.localidad_fiscal AS 'localidad'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.subTotal AS MONEY),1))) AS 'subtotal'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.iva AS MONEY),1))) AS 'iva'
		, CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(p.total AS MONEY),1))) AS 'total'
		, p.nota1 AS 'nota1'
		, p.nota2 AS 'nota2'		
		 , dbo.CalculoComprobante(tcmp.nombreAbreviado, '0', p.numeroComprobante) AS 'numeroProforma'		 
	FROM pedidos AS p			
	INNER JOIN clientes AS c ON p.id_cliente = c.id_cliente
	INNER JOIN comprobantes AS cmp ON p.id_comprobante = cmp.id_comprobante 
	INNER JOIN tipos_comprobantes AS tcmp ON cmp.id_tipoComprobante = tcmp.id_tipoComprobante 
	INNER JOIN provincias AS pro ON c.id_provincia_fiscal = pro.id_provincia	
	WHERE p.id_pedido = @idfc	
END
GO
/****** Object:  StoredProcedure [dbo].[SP_proforma_detalle]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_proforma_detalle]
	-- Add the parameters for the stored procedure here
	@idfc INTEGER
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT CASE WHEN pit.id_item IS NOT NULL THEN i.item END AS 'item_code', 
		CASE WHEN pit.id_item IS NULL THEN pit.descript ELSE i.descript END AS 'item_desc',		
		CASE WHEN (i.esDescuento = '0' AND i.esMarkup = '0') OR pit.id_item IS NULL THEN dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(pit.cantidad AS INT),1)) END AS 'item_qty', 
		CASE WHEN (i.esDescuento = '0' AND i.esMarkup = '0') OR pit.id_item IS NULL THEN CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(pit.precio AS MONEY),1))) END 'item_price', 
		CONCAT('$', dbo.milesArgentinos(CONVERT(VARCHAR(50), CAST(pit.cantidad * pit.precio AS MONEY),1))) AS 'item_subtotal'		 
	FROM pedidos_items AS pit
	LEFT JOIN items AS i ON pit.id_item = i.id_item
	WHERE pit.id_pedido = @idfc	
	ORDER BY i.esDescuento, i.esMarkup ASC
	--ORDER BY pit.id_pedidoItem ASC
END
GO
/****** Object:  StoredProcedure [dbo].[SP_updateAsocItemsProduccionTMP]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[SP_updateAsocItemsProduccionTMP]
	-- Add the parameters for the stored procedure here	
	@id_tmpProduccion_asocItem AS INTEGER,
	@id_tmpProduccionItem AS INTEGER,
	@id_item AS INTEGER,
	@id_item_asoc AS INTEGER,		
	@cantidad_item_asoc_enviada AS INTEGER,	
	@resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;

	UPDATE tmpproduccion_asocItems SET
		id_tmpProduccionItem = @id_tmpProduccionItem,
		id_item = @id_item, 
		id_item_asoc = @id_item_asoc,
		cantidad_item_asoc_enviada = @cantidad_item_asoc_enviada

	SET @resultado = @id_tmpProduccionItem

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_updateComprobanteCompra]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_updateComprobanteCompra]
	-- Add the parameters for the stored procedure here
	@id_comprobanteCompra AS INTEGER,
	@fecha_comprobante AS NVARCHAR(100),
	@id_proveedor AS INTEGER,
	@id_cc AS DECIMAL(18,3),
	@id_condicion_compra AS INTEGER,
	@id_tipoComprobante AS INTEGER,
	@id_moneda AS DECIMAL(18,3),
	@tasaCambio AS DECIMAL(18,3),
	@puntoVenta AS INTEGER,
	@numeroComprobante AS INTEGER,
	@cae AS NVARCHAR(50)
AS
BEGIN	
	SET NOCOUNT ON;
	SET DATEFORMAT dmy;
	UPDATE comprobantes_compras 
		SET fecha_comprobante = @fecha_comprobante,
		id_tipoComprobante = @id_tipoComprobante, 
		id_proveedor = @id_proveedor,
		id_cc = @id_cc, 
		id_moneda = @id_moneda,		
		puntoVenta = @puntoVenta, 
		numeroComprobante = @numeroComprobante,
		id_condicion_compra = @id_condicion_compra, 
		tasaCambio = @tasaCambio,
		cae = @cae
	WHERE id_comprobanteCompra = @id_comprobanteCompra	
END
GO
/****** Object:  StoredProcedure [dbo].[SP_updateItemsOCTMP]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_updateItemsOCTMP]
	-- Add the parameters for the stored procedure here	
	@id_tmpOCItem AS INTEGER,
	@id_item AS INTEGER,
	@cantidad AS INTEGER,	
	@precio AS DECIMAL(18,3),
	@descript AS NVARCHAR(100),
	@resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;

	UPDATE tmpOC_items SET
		id_item = @id_item,
		cantidad = @cantidad,
		precio = @precio,
		descript = @descript
	WHERE id_tmpOCItem = @id_tmpOCItem

	SET @resultado = @id_tmpOCItem

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_updateItemsProduccionTMP]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_updateItemsProduccionTMP]
	-- Add the parameters for the stored procedure here	
	@id_tmpProduccionItem AS INTEGER
	, @id_item AS INTEGER
	, @cantidad AS INTEGER
	, @descript AS NVARCHAR(100)
	, @id_usuario AS INTEGER
	, @resultado AS INTEGER OUTPUT
AS
BEGIN	
	SET NOCOUNT ON;

	UPDATE tmpproduccion_items SET
		id_item = @id_item
		, cantidad = @cantidad
		, descript = @descript	
		, id_usuario = @id_usuario

	SET @resultado = @id_tmpProduccionItem

	RETURN @resultado
END
GO
/****** Object:  StoredProcedure [dbo].[SP_updateItemsTMP]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_updateItemsTMP]
	-- Add the parameters for the stored procedure here
	@id_tmpPedidoItem AS INTEGER
	, @id_item AS INTEGER
	, @cantidad AS INTEGER
	, @precio AS DECIMAL(18,2)
	, @descript AS NVARCHAR(100)
	, @item AS NVARCHAR(50)
	, @id_usuario AS INTEGER
	, @id_unico AS NVARCHAR(MAX)
	, @resultado AS INTEGER OUTPUT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    IF @item = 'MANUAL' 
		BEGIN
			UPDATE tmppedidos_items SET descript = @descript, cantidad = @cantidad, precio = @precio, activo = 1 WHERE id_tmpPedidoItem = @id_tmpPedidoItem
		END
	ELSE
		BEGIN
			UPDATE tmppedidos_items SET id_item = @id_item, cantidad = @cantidad, precio = @precio, activo = 1 WHERE id_tmpPedidoItem = @id_tmpPedidoItem			
	END

	
	SET @resultado = 1
	RETURN
END
GO
/****** Object:  Trigger [dbo].[Ajuste_Stock]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE TRIGGER [dbo].[Ajuste_Stock]
   ON [dbo].[ajustes_stock]
   FOR INSERT
   AS    
   
	UPDATE i
	SET i.cantidad = i.cantidad + ins.cantidad
	FROM items AS i
	INNER JOIN INSERTED AS ins ON ins.id_item = i.id_item
GO
ALTER TABLE [dbo].[ajustes_stock] ENABLE TRIGGER [Ajuste_Stock]
GO
/****** Object:  Trigger [dbo].[No_borrar_ultima_CC_cliente]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[No_borrar_ultima_CC_cliente] ON [dbo].[cc_clientes]
INSTEAD OF DELETE 
AS 
BEGIN
  DELETE FROM cc_clientes WHERE (    
		SELECT COUNT(d.id_cc) 
		FROM Deleted d 
		INNER JOIN cc_clientes AS b ON d.id_cliente = b.id_cliente       
	) > 1 AND id_cc = (
		SELECT dd.id_cc 
		FROM deleted dd
	);
END;
GO
ALTER TABLE [dbo].[cc_clientes] ENABLE TRIGGER [No_borrar_ultima_CC_cliente]
GO
/****** Object:  Trigger [dbo].[No_borrar_ultima_CC_proveedor]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[No_borrar_ultima_CC_proveedor] ON [dbo].[cc_proveedores]
INSTEAD OF DELETE 
AS 
BEGIN
  DELETE FROM cc_clientes WHERE (    
		SELECT COUNT(d.id_cc) 
		FROM Deleted d 
		INNER JOIN cc_proveedores AS b ON d.id_proveedor = b.id_proveedor
	) > 1 AND id_cc = (
		SELECT dd.id_cc 
		FROM deleted dd
	);
END;
GO
ALTER TABLE [dbo].[cc_proveedores] ENABLE TRIGGER [No_borrar_ultima_CC_proveedor]
GO
/****** Object:  Trigger [dbo].[creaCCCliente]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[creaCCCliente]
   ON [dbo].[clientes]
   AFTER INSERT
   AS
   BEGIN
	DECLARE @id_cliente AS INTEGER
	SET NOCOUNT ON;
	SELECT @id_cliente = id_cliente FROM inserted

	INSERT INTO cc_clientes (id_cliente, id_moneda, nombre, saldo, activo) 
		VALUES (@id_cliente, 1, 'Default', 0, 1)
   END 
GO
ALTER TABLE [dbo].[clientes] ENABLE TRIGGER [creaCCCliente]
GO
/****** Object:  Trigger [dbo].[activaImpuesto]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[activaImpuesto]
ON [dbo].[impuestos]
FOR UPDATE
AS 
	DECLARE @id_impuesto AS INTEGER
	DECLARE @activo AS INTEGER

	SELECT @id_impuesto = id_impuesto FROM inserted
	SELECT @activo = activo FROM inserted

	IF UPDATE(activo)
	BEGIN
		UPDATE items_impuestos
		SET activo = @activo
		WHERE id_impuesto = @id_impuesto
	END
GO
ALTER TABLE [dbo].[impuestos] DISABLE TRIGGER [activaImpuesto]
GO
/****** Object:  Trigger [dbo].[CrearItems_Impuestos]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[CrearItems_Impuestos]
   ON [dbo].[impuestos]
   FOR INSERT
   AS
   
	INSERT INTO items_impuestos (id_impuesto, id_item, activo)
		SELECT ii.id_impuesto, i.id_item, ii.activo
		FROM items AS i
		JOIN impuestos AS ii ON ii.id_impuesto = ii.id_impuesto 
		INNER JOIN INSERTED AS ins ON ii.id_impuesto = ins.id_impuesto
GO
ALTER TABLE [dbo].[impuestos] DISABLE TRIGGER [CrearItems_Impuestos]
GO
/****** Object:  Trigger [dbo].[BorrarItem_Impuesto]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[BorrarItem_Impuesto]
   ON [dbo].[items]
   FOR DELETE
   AS
   
	DELETE FROM items_impuestos 
	WHERE id_item IN (SELECT id_item FROM deleted)
GO
ALTER TABLE [dbo].[items] DISABLE TRIGGER [BorrarItem_Impuesto]
GO
/****** Object:  Trigger [dbo].[CrearItem_Impuesto]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[CrearItem_Impuesto]
   ON [dbo].[items]
   FOR INSERT
   AS

	INSERT INTO items_impuestos (id_item, id_impuesto, activo) 
		SELECT i.id_item, ii.id_impuesto, ii.activo
		FROM items AS i
		JOIN items_impuestos AS ii ON ii.id_impuesto = ii.id_impuesto
		INNER JOIN INSERTED AS ins ON i.id_item = ins.id_item
		--WHERE ii.activo = '1'
GO
ALTER TABLE [dbo].[items] DISABLE TRIGGER [CrearItem_Impuesto]
GO
/****** Object:  Trigger [dbo].[ingresoPresupuesto]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[ingresoPresupuesto]
   ON [dbo].[pedidos]
   AFTER INSERT, UPDATE
   AS
   DECLARE @esPresupuesto AS BIT
   DECLARE @idUltimoPresupuesto AS INTEGER
   
   SELECT @esPresupuesto = esPresupuesto
   FROM INSERTED;

   IF @esPresupuesto = 1 
	SELECT @idUltimoPresupuesto = dbo.idUltimoPresupuesto() + 1
	IF @idUltimoPresupuesto = 0 OR @idUltimoPresupuesto = 1
		SET @idUltimoPresupuesto = 99999
	UPDATE p SET p.idPresupuesto = @idUltimoPresupuesto
		FROM pedidos AS p
	INNER JOIN DELETED as d ON d.id_pedido = p.id_pedido
GO
ALTER TABLE [dbo].[pedidos] DISABLE TRIGGER [ingresoPresupuesto]
GO
/****** Object:  Trigger [dbo].[Debitar_Stock]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[Debitar_Stock]
   ON [dbo].[pedidos_items]
   FOR INSERT
   AS

   UPDATE i SET i.cantidad = i.cantidad - ins.cantidad
   FROM items AS i   
   INNER JOIN INSERTED AS ins ON i.id_item = ins.id_item
   INNER JOIN pedidos AS p ON ins.id_pedido = p.id_pedido
   INNER JOIN comprobantes AS c ON p.id_comprobante = c.id_comprobante
   WHERE c.mueveStock = 1
GO
ALTER TABLE [dbo].[pedidos_items] ENABLE TRIGGER [Debitar_Stock]
GO
/****** Object:  Trigger [dbo].[Regresar_Stock]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[Regresar_Stock]
   ON [dbo].[pedidos_items]
   FOR DELETE
   AS

   UPDATE i SET i.cantidad = i.cantidad + del.cantidad
   FROM items AS i
   INNER JOIN DELETED AS del ON i.id_item = del.id_item
   INNER JOIN pedidos AS p ON del.id_pedido = p.id_pedido
   INNER JOIN comprobantes AS c ON p.id_comprobante = c.id_comprobante
   WHERE c.mueveStock = 1
GO
ALTER TABLE [dbo].[pedidos_items] ENABLE TRIGGER [Regresar_Stock]
GO
/****** Object:  Trigger [dbo].[Update_Stock]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[Update_Stock]
   ON [dbo].[pedidos_items]
   FOR UPDATE
   AS    

  	UPDATE i SET i.cantidad = i.cantidad + del.cantidad
	FROM items AS i
	INNER JOIN DELETED AS del ON i.id_item = del.id_item
	INNER JOIN pedidos AS p ON del.id_pedido = p.id_pedido
	INNER JOIN comprobantes AS c ON p.id_comprobante = c.id_comprobante
	WHERE c.mueveStock = 1

	UPDATE i SET i.cantidad = i.cantidad - ins.cantidad
	FROM items AS i
	INNER JOIN INSERTED AS ins ON i.id_item = ins.id_item
	INNER JOIN pedidos AS p ON ins.id_pedido = p.id_pedido
	INNER JOIN comprobantes AS c ON p.id_comprobante = c.id_comprobante
	WHERE c.mueveStock = 1
GO
ALTER TABLE [dbo].[pedidos_items] ENABLE TRIGGER [Update_Stock]
GO
/****** Object:  Trigger [dbo].[Update_Stock_Produccion]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[Update_Stock_Produccion]
   ON [dbo].[produccion_items]
   FOR UPDATE
   AS    

  	/*UPDATE i
		SET i.cantidad = i.cantidad + d.cantidad
	FROM items AS i
	INNER JOIN DELETED AS d on i.id_item = d.id_item*/

	UPDATE i
		SET i.cantidad = i.cantidad + d.cantidad_recibida
	FROM items AS i
	INNER JOIN INSERTED AS d ON i.id_item = d.id_item_recibido
	WHERE d.activo = 0

	UPDATE ii
		SET ii.cantidad = ii.cantidad - pai.cantidad_item_asoc_enviada
	FROM items AS i
	INNER JOIN INSERTED AS d ON i.id_item = d.id_item_recibido
	INNER JOIN produccion_asocItems AS pai ON d.id_produccion = pai.id_produccion
	INNER JOIN items AS ii ON pai.id_item_asoc = ii.id_item
	WHERE d.activo = 0 AND d.id_item_recibido IS NOT NULL

	
GO
ALTER TABLE [dbo].[produccion_items] ENABLE TRIGGER [Update_Stock_Produccion]
GO
/****** Object:  Trigger [dbo].[creaCCProveedor]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[creaCCProveedor]
   ON [dbo].[proveedores]
   AFTER INSERT
   AS
   BEGIN
	DECLARE @id_proveedor AS INTEGER
	SET NOCOUNT ON;
	SELECT @id_proveedor = id_proveedor FROM inserted

	INSERT INTO cc_proveedores(id_proveedor, id_moneda, nombre, saldo, activo) 
		VALUES (@id_proveedor, 1, 'Default', 0, 1)
   END 
GO
ALTER TABLE [dbo].[proveedores] ENABLE TRIGGER [creaCCProveedor]
GO
/****** Object:  Trigger [dbo].[UpdateItems]    Script Date: 17/7/2025 14:18:31 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[UpdateItems]
   ON [dbo].[registros_stock]
   FOR INSERT
   AS
   UPDATE p SET p.cantidad = p.cantidad + d.cantidad, p.costo = d.costo,
    p.precio_lista = d.precio_lista, p.factor = d.factor
   FROM items AS p
   INNER JOIN INSERTED AS d ON d.id_item = p.id_item
GO
ALTER TABLE [dbo].[registros_stock] ENABLE TRIGGER [UpdateItems]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[40] 4[20] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1[50] 2[25] 3) )"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "cheques"
            Begin Extent = 
               Top = 13
               Left = 94
               Bottom = 342
               Right = 279
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "cuentas_bancarias"
            Begin Extent = 
               Top = 104
               Left = 526
               Bottom = 326
               Right = 699
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "bancos"
            Begin Extent = 
               Top = 29
               Left = 851
               Bottom = 235
               Right = 1021
            End
            DisplayFlags = 280
            TopColumn = 0
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 1440
         Alias = 900
         Table = 1170
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1350
         SortOrder = 1410
         GroupBy = 1350
         Filter = 1350
         Or = 1350
         Or = 2235
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'cheques_a_cobrar'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'cheques_a_cobrar'
GO
USE [master]
GO
ALTER DATABASE [dbCentrex] SET  READ_WRITE 
GO
