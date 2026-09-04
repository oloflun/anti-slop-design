// React Theme — extracted from https://mode.com
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '22': string;
    '24': string;
    '36': string;
    '56': string;
    '70': string;
    '72': string;
    '96': string;
    '153.6': string;
 *   };
 *   space: {
    '2': string;
    '8': string;
    '36': string;
    '40': string;
    '50': string;
    '55': string;
    '60': string;
    '90': string;
    '100': string;
    '120': string;
    '130': string;
    '200': string;
    '240': string;
 *   };
 *   radii: {
    xs: string;
    sm: string;
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
    md: string;
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
    "primary": "#c8f169",
    "secondary": "#043f2e",
    "accent": "#1863dc",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#212121",
    "neutral200": "#fcfcfc",
    "neutral300": "#f4f4f4",
    "neutral400": "#d0d5d2"
  },
  "fonts": {
    "body": "'--fonts-sans', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "22": "22px",
    "24": "24px",
    "36": "36px",
    "56": "56px",
    "70": "70px",
    "72": "72px",
    "96": "96px",
    "153.6": "153.6px"
  },
  "space": {
    "2": "2px",
    "8": "8px",
    "36": "36px",
    "40": "40px",
    "50": "50px",
    "55": "55px",
    "60": "60px",
    "90": "90px",
    "100": "100px",
    "120": "120px",
    "130": "130px",
    "200": "200px",
    "240": "240px"
  },
  "radii": {
    "xs": "2px",
    "sm": "5px",
    "md": "8px",
    "lg": "16px",
    "full": "50px"
  },
  "shadows": {
    "md": "rgba(172, 171, 171, 0.3) 0px -1px 10px 0px",
    "xl": "rgba(0, 0, 0, 0.3) 0px 32px 68px 0px"
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
      "main": "#c8f169",
      "light": "hsl(78, 83%, 83%)",
      "dark": "hsl(78, 83%, 53%)"
    },
    "secondary": {
      "main": "#043f2e",
      "light": "hsl(163, 88%, 28%)",
      "dark": "hsl(163, 88%, 10%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#c8f169"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#212121"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "400",
      "lineHeight": "37.08px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(172, 171, 171, 0.3) 0px -1px 10px 0px",
    "rgba(0, 0, 0, 0.3) 0px 32px 68px 0px"
  ]
};

export default theme;
