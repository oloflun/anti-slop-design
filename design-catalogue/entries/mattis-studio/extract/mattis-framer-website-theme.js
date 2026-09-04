// React Theme — extracted from https://mattis.framer.website/
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '16': string;
    '18': string;
    '20': string;
    '26': string;
    '32': string;
    '34': string;
    '58': string;
    '64': string;
    '78': string;
    '92': string;
    '100': string;
    '140.498': string;
 *   };
 *   space: {
    '1': string;
    '30': string;
    '36': string;
    '40': string;
    '50': string;
    '60': string;
    '70': string;
    '80': string;
    '90': string;
    '100': string;
    '110': string;
    '120': string;
    '130': string;
 *   };
 *   radii: {
    md: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    xs: string;
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
    "primary": "#ff4500",
    "secondary": "#0000ee",
    "accent": "#d2ff37",
    "background": "#0b0b0b",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#0b0b0b",
    "neutral300": "#e9e9e9",
    "neutral400": "#767676",
    "neutral500": "#181818",
    "neutral600": "#222222"
  },
  "fonts": {
    "body": "'Times New Roman', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "26": "26px",
    "32": "32px",
    "34": "34px",
    "58": "58px",
    "64": "64px",
    "78": "78px",
    "92": "92px",
    "100": "100px",
    "140.498": "140.498px"
  },
  "space": {
    "1": "1px",
    "30": "30px",
    "36": "36px",
    "40": "40px",
    "50": "50px",
    "60": "60px",
    "70": "70px",
    "80": "80px",
    "90": "90px",
    "100": "100px",
    "110": "110px",
    "120": "120px",
    "130": "130px"
  },
  "radii": {
    "md": "10px",
    "full": "100px"
  },
  "shadows": {
    "sm": "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "xs": "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
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
      "main": "#ff4500",
      "light": "hsl(16, 100%, 65%)",
      "dark": "hsl(16, 100%, 35%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#0b0b0b",
      "paper": "#ffffff"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "58px",
      "fontWeight": "600",
      "lineHeight": "normal"
    }
  },
  "shape": {
    "borderRadius": 7
  },
  "shadows": [
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
  ]
};

export default theme;
