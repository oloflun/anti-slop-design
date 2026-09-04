// React Theme — extracted from https://www.harkcap.com
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
    '12': string;
    '14': string;
    '16': string;
    '229.231': string;
    '86.3077': string;
    '53.2308': string;
    '44.3077': string;
    '28.6154': string;
    '21.8462': string;
    '17.8462': string;
 *   };
 *   space: {
    '2': string;
    '36': string;
    '42': string;
    '58': string;
    '63': string;
    '74': string;
    '86': string;
    '110': string;
    '115': string;
    '131': string;
    '177': string;
    '196': string;
    '457': string;
    '473': string;
    '490': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    full: string;
 *   };
 *   shadows: {

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
    "primary": "#114167",
    "secondary": "#00f2e5",
    "accent": "#235e80",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#181818",
    "neutral100": "#ffffff",
    "neutral200": "#f3f3f3",
    "neutral300": "#919598",
    "neutral400": "#000000",
    "neutral500": "#232323",
    "neutral600": "#d4d4d4"
  },
  "fonts": {
    "body": "'Suisseworks Webs', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "229.231": "229.231px",
    "86.3077": "86.3077px",
    "53.2308": "53.2308px",
    "44.3077": "44.3077px",
    "28.6154": "28.6154px",
    "21.8462": "21.8462px",
    "17.8462": "17.8462px"
  },
  "space": {
    "2": "2px",
    "36": "36px",
    "42": "42px",
    "58": "58px",
    "63": "63px",
    "74": "74px",
    "86": "86px",
    "110": "110px",
    "115": "115px",
    "131": "131px",
    "177": "177px",
    "196": "196px",
    "457": "457px",
    "473": "473px",
    "490": "490px"
  },
  "radii": {
    "sm": "3px",
    "md": "6px",
    "full": "1280px"
  },
  "shadows": {},
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
      "main": "#114167",
      "light": "hsl(207, 72%, 39%)",
      "dark": "hsl(207, 72%, 10%)"
    },
    "secondary": {
      "main": "#00f2e5",
      "light": "hsl(177, 100%, 62%)",
      "dark": "hsl(177, 100%, 32%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#f3f3f3"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#181818"
    }
  },
  "typography": {
    "fontFamily": "'Aeonikpro', sans-serif",
    "h1": {
      "fontSize": "44.3077px",
      "fontWeight": "400",
      "lineHeight": "44.3077px"
    },
    "h2": {
      "fontSize": "28.6154px",
      "fontWeight": "400",
      "lineHeight": "31.4769px"
    },
    "h3": {
      "fontSize": "21.8462px",
      "fontWeight": "400",
      "lineHeight": "26.2154px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": []
};

export default theme;
