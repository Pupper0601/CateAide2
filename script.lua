address = "C:/CuteAide/output.lua"

-- 计算后坐力
function calculate_influencing_factor()
    dofile(address)
    calculation_results = coefficient
    if in_car == "yes" then
        -- 在车上
        calculation_results = calculation_results * car
    end

    if IsModifierPressed("lshift") then
        -- 按住左shift
        calculation_results = calculation_results * global_lshift
    end
    return calculation_results
end

local debug = false

local cumulative_recoil = 0 -- 累计后坐力

Cumulative = function(_data)
    -- 累计后坐力
    cumulative_recoil = cumulative_recoil + (_data * calculate_influencing_factor())
    adjusted_recoil = math.floor(cumulative_recoil)
    cumulative_recoil = cumulative_recoil - adjusted_recoil
    if adjusted_recoil < 1 then
        adjusted_recoil = 1
    end
    return adjusted_recoil
end

-- 开始压枪
Auto_Down = function()
    dofile(address)
    ClearLog()
    if coefficient == "none" then
        OutputLogMessage("当前武器不支持压枪: %s\n", weapon)
        return
    end
    if weapon == nil or weapon == "weapon_none" then
        OutputLogMessage("请先读取武器参数或当前武器为 weapon_none \n")
        return
    end

    -- 特殊武器
    _weapons = {ZDZT = true,MINI14 = true,SKS = true,VSS = true,QBU = true,MK14 = true,MK12 = true,DLGNF = true,M16A4 = true,MK47 = true}
    if _weapons[weapon] then
        OutputLogMessage("当前武器不支持压枪: %s\n", weapon)
        return
    end

    local _number_bullets = 0   -- 子弹数
     local nowTime = GetRunningTime() -- 获取当前时间

    for _, recoil_data in ipairs(guns_trajectory) do
        while IsMouseButtonPressed(1) and shooting_state == "1" do
            for i=1, 4 do
                adjusted_recoil = Cumulative(recoil_data[2])  -- 调整后的后坐力
                 MoveMouseRelative(0, adjusted_recoil)  -- 移动鼠标

                delay(weapon_intervals / 4 )    -- 延迟
                --OutputLogMessage("当前时间 %s, 初始时间: %s, 差值: %s\n", GetRunningTime(), nowTime, GetRunningTime() - nowTime)

                OutputLogMessage("当前子弹数: %s, 后坐力: %s, 系数: %s, 下压像素: %s\n",
                                     recoil_data[1], recoil_data[2],
                                     calculate_influencing_factor(), adjusted_recoil)

                if not IsMouseButtonPressed(1) then
                    break
                end
                i = i + 1
            end
            break
        end
    end
end

local cumulative_time = 0  -- 累计时间

delay = function(wait)
    _time = wait + cumulative_time
    s, f = math.modf(_time) -- 整数部分和小数部分
    cumulative_time = cumulative_time + f
    if cumulative_time >= 1 then
        cumulative_time = cumulative_time - 1
        s = s + 1
    end
    Sleep(s)
end


-- 事件处理
function OnEvent(event, key)
    dofile(address)

    if event == "MOUSE_BUTTON_PRESSED" and key == 1 then

        if opening_method == "click" then
            -- 点击开镜
            delay(27)
            Auto_Down()
        elseif opening_method == "long_press" and IsMouseButtonPressed(3) then
            -- 长按开镜
            delay(27)
            Auto_Down()
        end
    end
end

ClearLog()
OutputLogMessage("%s", "运行成功\n")
EnablePrimaryMouseButtonEvents(true)
math.randomseed(GetDate("%H%M%S"):reverse())

function G1_PRESSED()
    G1___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 1, "mouse")
end
function G1_RELEASED()
    G1___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 1, "mouse")
end
function G2_PRESSED()
    G2___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 2, "mouse")
end
function G2_RELEASED()
    G2___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 2, "mouse")
end
function G3_PRESSED()
    G3___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 3, "mouse")
end
function G3_RELEASED()
    G3___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 3, "mouse")
end
function G4_PRESSED()
    G4___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 4, "mouse")
end
function G4_RELEASED()
    G4___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 4, "mouse")
end
function G5_PRESSED()
    G5___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 5, "mouse")
end
function G5_RELEASED()
    G5___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 5, "mouse")
end
while true do
    while IsMouseButtonPressed(1) and not G1___ do
        G1_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(1) and G1___ do
        G1_RELEASED()
        break
        Sleep(1)
    end
    while IsMouseButtonPressed(3) and not G2___ do
        G2_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(3) and G2___ do
        G2_RELEASED()
        break
        Sleep(1)
    end
    while IsMouseButtonPressed(2) and not G3___ do
        G3_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(2) and G3___ do
        G3_RELEASED()
        break
        Sleep(1)
    end
    while IsMouseButtonPressed(4) and not G4___ do
        G4_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(4) and G4___ do
        G4_RELEASED()
        break
        Sleep(1)
    end
    while IsMouseButtonPressed(5) and not G5___ do
        G5_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(5) and G5___ do
        G5_RELEASED()
        break
        Sleep(1)
    end
    Sleep(1)
end