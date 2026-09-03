import React from 'react'
import useTheme from '../contexts/theme';

export default function ThemeBtn() {
    
    const {themeMode, lightTheme, darkTheme} = useTheme()
    const onChangeBtn = (e) => {
        const darkModeStatus = e.currentTarget.checked
        console.log("Dark Mode Status: ", darkModeStatus)
        if (darkModeStatus) {
            darkTheme()
        } else {
            lightTheme()
        }
    }
    return (
    <label className="relative inline-flex items-center cursor-pointer p-4 bg-blue-200 rounded-xl border-4 border-blue-600 shadow-lg">
            <input
                type="checkbox"
                value=""
                className="sr-only peer"
                onChange={onChangeBtn}
                checked={themeMode=== "dark"}
            />
            <div className="w-14 h-8 bg-white peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-400 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-blue-600 after:border-blue-600 after:border after:rounded-full after:h-7 after:w-7 after:transition-all dark:border-gray-600 peer-checked:bg-blue-700 border border-blue-600"></div>
            <span className="ml-5 text-lg font-extrabold text-blue-900">Toggle Theme</span>
        </label>
    );
}
