--Gatterschaltung zu Aufgabe 2.4
--Christian Rebischke 18.4.2014
-- x Eingänge, y Ausgang, z "zwischenstationen"
library IEEE;
use IEEE.std_logic_1164.all;

entity Gatterschaltung is
  port(x: in STD_LOGIC_VECTOR(2 DOWNTO 0);
        y: out STD_LOGIC);
end entity;

architecture test of Gatterschaltung is
  signal z: STD_LOGIC_VECTOR(4 DOWNTO 0);
begin
  z(0) <= not(x(1));
  z(1) <= not(x(2));
  z(2) <= x(0) nand x(1);
  z(3) <= x(0) nand (z(0) and x(2));
  z(4) <= x(0) nand z(1);
  y <= z(2) nand (z(3) and z(4));
end architecture;

