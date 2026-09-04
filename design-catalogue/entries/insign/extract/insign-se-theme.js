// React Theme — extracted from https://www.insign.se
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
    heading: string;
 *   };
 *   fontSizes: {
    '16': string;
    '17': string;
    '18': string;
    '20': string;
    '28': string;
    '30': string;
    '36': string;
    '40': string;
    '50': string;
    '80': string;
    '76.8': string;
    '67.2': string;
 *   };
 *   space: {
    '2': string;
    '12': string;
    '14': string;
    '20': string;
    '22': string;
    '24': string;
    '29': string;
    '32': string;
    '36': string;
    '40': string;
    '46': string;
    '50': string;
    '67': string;
    '78': string;
    '80': string;
    '83': string;
 *   };
 *   radii: {
    xs: string;
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    xs: string;
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
    "primary": "#ff7f4c",
    "secondary": "#008000",
    "accent": "#0073aa",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#1a1819",
    "neutral200": "#ffffff",
    "neutral300": "#828282",
    "neutral400": "#181d27",
    "neutral500": "#8c8c8c",
    "neutral600": "#ecf1f7",
    "neutral700": "#c6c6c6",
    "neutral800": "#334155",
    "neutral900": "#414651"
  },
  "fonts": {
    "body": "'ETmodules', sans-serif",
    "heading": "'Neue Haas Grotesk RoundDots - 45 Light', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "17": "17px",
    "18": "18px",
    "20": "20px",
    "28": "28px",
    "30": "30px",
    "36": "36px",
    "40": "40px",
    "50": "50px",
    "80": "80px",
    "76.8": "76.8px",
    "67.2": "67.2px"
  },
  "space": {
    "2": "2px",
    "12": "12px",
    "14": "14px",
    "20": "20px",
    "22": "22px",
    "24": "24px",
    "29": "29px",
    "32": "32px",
    "36": "36px",
    "40": "40px",
    "46": "46px",
    "50": "50px",
    "67": "67px",
    "78": "78px",
    "80": "80px",
    "83": "83px"
  },
  "radii": {
    "xs": "1px",
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "xl": "20px",
    "full": "160px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0.02) 0px 4px 4px 0px",
    "xs": "rgba(10, 13, 18, 0.05) 0px 1px 2px 0px",
    "lg": "rgba(0, 0, 0, 0.19) 0px 10px 20px 0px, rgba(0, 0, 0, 0.23) 0px 6px 6px 0px",
    "xl": "rgba(0, 0, 0, 0.2) 2px 8px 60px -2px"
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
      "main": "#ff7f4c",
      "light": "hsl(17, 100%, 80%)",
      "dark": "hsl(17, 100%, 50%)"
    },
    "secondary": {
      "main": "#008000",
      "light": "hsl(120, 100%, 40%)",
      "dark": "hsl(120, 100%, 10%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#1a1819"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#1a1819"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "400",
      "lineHeight": "54px",
      "fontFamily": "'Neue Haas Grotesk RoundDots - 45 Light', sans-serif"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgb(26, 24, 25) 0px 0px 0px 1px",
    "rgb(65, 70, 81) 0px 0px 0px 1px",
    "rgba(10, 13, 18, 0.18) 0px 0px 0px 1px inset, rgba(10, 13, 18, 0.05) 0px -2px 0px 0px inset, rgba(10, 13, 18, 0.05) 0px 1px 2px 0px",
    "rgba(10, 13, 18, 0.05) 0px 1px 2px 0px",
    "rgba(0, 0, 0, 0.1) 0px 2px 5px 0px"
  ]
};

export default theme;
