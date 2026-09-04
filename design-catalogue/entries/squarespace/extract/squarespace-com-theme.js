// React Theme — extracted from https://www.squarespace.com
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
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
    '12': string;
    '13': string;
    '14': string;
    '15': string;
    '16': string;
    '20': string;
    '26': string;
    '36': string;
    '50': string;
    '60': string;
    '70': string;
 *   };
 *   space: {
    '2': string;
    '8': string;
    '40': string;
    '48': string;
    '52': string;
    '56': string;
    '63': string;
    '80': string;
    '120': string;
    '160': string;
    '240': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    lg: string;
    xl: string;
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
    "primary": "#200603",
    "secondary": "#1e4c41",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#898989",
    "neutral300": "#222222",
    "neutral400": "#2f2f2f",
    "neutral500": "#0e0e0e",
    "neutral600": "#e7e7e7",
    "neutral700": "#dddddd",
    "neutral800": "#5a5a5a",
    "neutral900": "#f5f5f4"
  },
  "fonts": {
    "body": "'ClarksonLight', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "13": "13px",
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "20": "20px",
    "26": "26px",
    "36": "36px",
    "50": "50px",
    "60": "60px",
    "70": "70px"
  },
  "space": {
    "2": "2px",
    "8": "8px",
    "40": "40px",
    "48": "48px",
    "52": "52px",
    "56": "56px",
    "63": "63px",
    "80": "80px",
    "120": "120px",
    "160": "160px",
    "240": "240px"
  },
  "radii": {
    "sm": "3px",
    "md": "6px",
    "lg": "16px",
    "full": "100px"
  },
  "shadows": {
    "sm": "color(srgb 0 0 0 / 0.2) 0px 0px 0px 2px inset",
    "lg": "rgba(0, 0, 0, 0.1) 0px 8px 16px 0px",
    "xl": "rgba(0, 0, 0, 0.05) 0px 134px 80px 0px, rgba(0, 0, 0, 0.09) 0px 60px 60px 0px, rgba(0, 0, 0, 0.1) 0px 15px 33px 0px"
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
      "main": "#200603",
      "light": "hsl(6, 83%, 22%)",
      "dark": "hsl(6, 83%, 10%)"
    },
    "secondary": {
      "main": "#1e4c41",
      "light": "hsl(166, 43%, 36%)",
      "dark": "hsl(166, 43%, 10%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "fontFamily": "'ClarksonLight', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "400",
      "lineHeight": "38.88px"
    },
    "h2": {
      "fontSize": "26px",
      "fontWeight": "400",
      "lineHeight": "28.08px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "500",
      "lineHeight": "24px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": [
    "color(srgb 1 1 1 / 0.2) 0px 0px 0px 2px inset",
    "color(srgb 0 0 0 / 0.2) 0px 0px 0px 2px inset",
    "rgba(0, 0, 0, 0.1) 0px 8px 16px 0px",
    "rgba(0, 0, 0, 0.05) 0px 23px 14px 0px, rgba(0, 0, 0, 0.09) 0px 10px 10px 0px, rgba(0, 0, 0, 0.1) 0px 3px 6px 0px",
    "rgba(0, 0, 0, 0.05) 0px 134px 80px 0px, rgba(0, 0, 0, 0.09) 0px 60px 60px 0px, rgba(0, 0, 0, 0.1) 0px 15px 33px 0px"
  ]
};

export default theme;
