--Aufgabe 4.4

library ieee;
use ieee.std_logic_1164.all;
use ieee.Numeric_STD.all;

entity Aufgabe4_4 is
  port(x: in STD_LOGIC_VECTOR(4 downto 1);
       y: out STD_LOGIC);
end entity;

architecture test of Aufgabe4_4 is
begin
  process(x)
    variable z: STD_LOGIC_VECTOR(2 DOWNTO 0);
  begin
    --Bereich links oben
    z(0) := x(1) and x(2);
    z(1) := x(1) or x(2);
    if x(3) = '0' then
      z(2) := z(0);
    else 
      z(2) := z(1);
    end if;
    --Abtastregister
    if RISING_EDGE(x(4)) then
      y <= z(2);
    end if;
  end process;
end architecture;

