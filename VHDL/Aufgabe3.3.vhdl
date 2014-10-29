--Gatterschaltung zu Aufgabe 3.3
--Christian Rebischke 30.4.2014
-- x Eingänge, y Ausgang, z "zwischenstationen"
library IEEE;
use IEEE.std_logic_1164.all;

entity Gatterschaltung is
  port(x: in STD_LOGIC_VECTOR(4 DOWNTO 1);
        y: out STD_LOGIC);
end entity;

architecture test of Gatterschaltung is
  signal z: STD_LOGIC;
begin
  z <= (x(1) and not x(2)) or (x(2) and x(3)) after 1 ns;
  y <= (z and not x(4)) or (x(4) and x(3)) after 1 ns;
end architecture;

