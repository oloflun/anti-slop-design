// React Theme — extracted from https://highwaymedia.se/webbyra-goteborg/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
    neutral900: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '22': string;
    '24': string;
    '26': string;
    '30': string;
    '34': string;
    '42': string;
    '54': string;
    '56': string;
    '60': string;
    '84': string;
    '102.4': string;
    '25.6': string;
 *   };
 *   space: {
    '0': string;
    '20': string;
    '25': string;
    '28': string;
    '40': string;
    '45': string;
    '50': string;
    '60': string;
    '70': string;
    '73': string;
    '100': string;
    '106': string;
    '120': string;
    '140': string;
    '200': string;
    '240': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    lg: string;
 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#624058",
    "secondary": "#ec8aa3",
    "accent": "#d4edda",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#232323",
    "neutral100": "#000000",
    "neutral200": "#ffffff",
    "neutral300": "#495057",
    "neutral400": "#929292",
    "neutral500": "#656565",
    "neutral600": "#dee2e6",
    "neutral700": "#cccccc",
    "neutral800": "#333333",
    "neutral900": "#ffe8ee"
  },
  "fonts": {
    "body": "'Open Sans', sans-serif"
  },
  "fontSizes": {
    "22": "22px",
    "24": "24px",
    "26": "26px",
    "30": "30px",
    "34": "34px",
    "42": "42px",
    "54": "54px",
    "56": "56px",
    "60": "60px",
    "84": "84px",
    "102.4": "102.4px",
    "25.6": "25.6px"
  },
  "space": {
    "0": "0px",
    "20": "20px",
    "25": "25px",
    "28": "28px",
    "40": "40px",
    "45": "45px",
    "50": "50px",
    "60": "60px",
    "70": "70px",
    "73": "73px",
    "100": "100px",
    "106": "106px",
    "120": "120px",
    "140": "140px",
    "200": "200px",
    "240": "240px"
  },
  "radii": {
    "sm": "3px",
    "md": "10px",
    "lg": "15px",
    "xl": "20px",
    "full": "100px"
  },
  "shadows": {
    "lg": "rgba(0, 0, 0, 0.1) 0px 0px 29px -4px"
  },
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#624058",
      "light": "hsl(318, 21%, 47%)",
      "dark": "hsl(318, 21%, 17%)"
    },
    "secondary": {
      "main": "#ec8aa3",
      "light": "hsl(345, 72%, 88%)",
      "dark": "hsl(345, 72%, 58%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#232323"
    }
  },
  "typography": {
    "fontFamily": "'Inter', sans-serif",
    "h1": {
      "fontSize": "42px",
      "fontWeight": "600",
      "lineHeight": "50.4px"
    }
  },
  "shape": {
    "borderRadius": 10
  },
  "shadows": [
    "rgba(0, 0, 0, 0.1) 0px 0px 29px -4px"
  ]
};

export default theme;
