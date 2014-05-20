--Aufgabe 4.3 

library ieee;
use ieee.std_logic_1164.all;
use ieee.Numeric_STD.all;

entity Aufgabe4_3 is
  port(a: in UNSIGNED(3 downto 0);
       b: in UNSIGNED(3 downto 0);
       s: in STD_LOGIC_VECTOR(1 DOWNTO 0);
       y: out UNSIGNED(3 downto 0));
end entity;

architecture test of Aufgabe4_3 is
begin
  process(a,b,s)
    variable v0,v1,v2,v3,v4: UNSIGNED(3 downto 0);
  begin
    --Linker Bereich + Oben Rechts
    v0 := a and b;
    v1 := a or b;
    if s(0) = '0' then
      v2 := v0;
      v3 := a;
    else 
      v2 := v1;
      v3 := not(a);
    end if;
    --Addierer / Links Unten
    v4 := v3 + b;
    if s(1) = '0' then
      y <= v2;
    else
      y <= v4;
    end if;
  end process;
end architecture;
    
    
    
